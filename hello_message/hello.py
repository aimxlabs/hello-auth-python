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

    def generate_hello_message(self, expires_in_seconds: int = 5):
        """
        Generate a hello message

        :return: A dictionary containing the message, nonce, and signature.
        """
        # Generate a nonce
        nonce = str(uuid.uuid4())

        # Generate an expiration timestamp
        expires = str(int(time.time() + expires_in_seconds))

        # Create the message
        message = f"hello:{nonce}:{expires}"

        # Sign the message
        signature = Account.sign_message(encode_defunct(text=message), private_key=self.private_key)

        # Create the hello message
        hello_message = {"message": message, "signature": signature.signature.hex(), "address": self.address}

        return base64.b64encode(json.dumps(hello_message).encode('utf-8')).decode('utf-8')

    @staticmethod
    def verify_signature(message:str):
        """
        Verify the authenticity of a "hello" message signature and validate the nonce.

        :param message: The base64 encoded "hello" message (in the format "hello:{nonce}:{expires}") containing signature and metadata.
        :return: A dictionary containing validation result, signer address and nonce.
        """
        try:
            # Decode and parse the message
            hello_message = json.loads(base64.b64decode(message).decode('utf-8'))

            # Validate message format
            if not len(hello_message["message"].split(":")) == 3:
                raise ValueError("Invalid message format")

            # Extract nonce and expires from the message
            message = hello_message["message"]
            nonce = hello_message["message"].split(":")[1]
            expires = hello_message["message"].split(":")[2]
            signature = hello_message["signature"]
            address = hello_message["address"]

            # Verify that nonce is a valid uuid
            if not uuid.UUID(nonce):
                raise ValueError("Invalid nonce format")

            # Verify that expires is a valid timestamp
            if not expires.isdigit():
                raise ValueError("Invalid expires format")

            # Verify signature and recover signer
            message_hash = encode_defunct(text=message)
            recovered_address = Account.recover_message(
                message_hash, 
                signature=signature
            )

            # Verify the current time is before the expiration timestamp
            is_not_expired = int(time.time()) < int(expires)

            # Verify recovered address matches claimed address
            is_valid = is_not_expired and recovered_address.lower() == address.lower()

            return {
                "valid": is_valid,
                "address": address, 
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