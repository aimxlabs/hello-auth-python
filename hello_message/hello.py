import uuid
import json
import base64
import time
from eth_account import Account
from eth_account.messages import encode_defunct

class Hello:
    def __init__(self, key_provider: callable):
        """
        Initialize the Hello message generator with a private key.

        :param key_provider: A callable that returns an Ethereum private key for signing messages.
        """
        self.key_provider = key_provider
        self.address = Account.from_key(self.key_provider()).address

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
        message_text = f"hello:{nonce}:{expires}"

        # Sign the message
        signature = Account.sign_message(encode_defunct(text=message_text), private_key=self.key_provider())

        # Create the hello message
        hello_message = {"message": message_text, "signature": signature.signature.hex(), "address": self.address}

        return base64.b64encode(json.dumps(hello_message).encode('utf-8')).decode('utf-8')

    @staticmethod
    def verify_signature(hello_message:str):
        """
        Verify the authenticity of a "hello" message signature and validate the nonce.

        :param hello_message: The base64 encoded "hello" message (in the format "hello:{nonce}:{expires}") containing signature and metadata.
        :return: A dictionary containing validation result, signer address and nonce.
        """

        # Decode the message
        message_dict = json.loads(base64.b64decode(hello_message).decode('utf-8'))

        # Check that the message contains the required fields
        if not all(k in message_dict for k in ("message", "signature", "address")):
            raise ValueError("Missing required fields in hello message")

        # Check that the signature length is 130 bytes (65 bytes * 2 for r and s)
        if len(message_dict["signature"]) != 130:
            raise ValueError("Invalid signature length")

        # Validate message format
        parts = message_dict["message"].split(":")
        if len(parts) != 3 or parts[0] != "hello":
            raise ValueError("Invalid message format")

        # Extract message data
        message_text = message_dict["message"]
        nonce = message_dict["message"].split(":")[1]
        expires = message_dict["message"].split(":")[2]
        signature = message_dict["signature"]
        address = message_dict["address"]

        # Verify that nonce is a valid uuid
        if not uuid.UUID(nonce):
            raise ValueError("Invalid nonce format")

        # Verify that expires is a valid timestamp
        if not expires.isdigit():
            raise ValueError("Invalid expires format")

        try:
            # Verify signature and recover signer
            recovered_address = Account.recover_message(
                encode_defunct(text=message_text), 
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