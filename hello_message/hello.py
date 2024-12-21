import uuid
import json
import base64
import time
from eth_account import Account
from eth_account.messages import encode_defunct

class Hello:
    def __init__(self, private_key: str):
        """
        Initialize the Hello message generator with a private key.

        :param private_key: Ethereum private key for signing messages.
        """
        self.private_key = private_key
        self.address = Account.from_key(private_key).address

    def get_address(self) -> str:
        """
        Get the Ethereum address corresponding to the private key.

        :return: Ethereum address as a string.
        """
        return self.address

    def generate_hello_message(self):
        """
        Generate a hello message

        :return: A dictionary containing the message, nonce, and signature.
        """
        nonce = str(uuid.uuid4())
        expiration_timestamp = str(int(time.time() + 5)) # Add an expiration timestamp 5 seconds from now
        message = f"hello:{nonce}:{expiration_timestamp}"
        message_hash = encode_defunct(text=message)
        signature = Account.sign_message(message_hash, private_key=self.private_key)
        generated_message = {"message": message, "signature": signature.signature.hex(), "address": self.address}
        result = base64.b64encode(json.dumps(generated_message).encode('utf-8')).decode('utf-8')

        return result

    @staticmethod
    def verify_signature(message:str):
        """
        Verify the authenticity of a "hello" message signature and validate the nonce.

        :param message: The base64 encoded "hello" message containing signature and metadata.
        :return: A dictionary containing validation result, signer address and nonce.
        """
        try:
            # Decode and parse the message
            hello_message = json.loads(base64.b64decode(message).decode('utf-8'))

            # Validate message format
            if not hello_message["message"].startswith("hello:"):
                raise ValueError("Invalid message format")

            nonce = hello_message["message"].split(":")[1]
            expires = hello_message["message"].split(":")[2]

            # Verify signature and recover signer
            message_hash = encode_defunct(text=hello_message["message"])
            recovered_address = Account.recover_message(
                message_hash, 
                signature=hello_message["signature"]
            )

            # Verify the current time is before the expiration timestamp
            is_valid_timestamp = int(time.time()) < int(expires)

            # Verify recovered address matches claimed address
            is_valid = is_valid_timestamp and recovered_address.lower() == hello_message["address"].lower()

            return {
                "valid": is_valid,
                "address": hello_message["address"], 
                "nonce": nonce,
                "expires": expires
            }

        except Exception as e:
            return {
                "valid": False,
                "address": None,
                "nonce": None,
                "expires": None,
                "error": str(e)
            }