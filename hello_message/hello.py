import uuid
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
        message = f"hello:{nonce}"
        message_hash = encode_defunct(text=message)
        signature = Account.sign_message(message_hash, private_key=self.private_key)
        return {"message": message, "nonce": nonce, "signature": signature.signature.hex()}

    @staticmethod
    def verify_signature(signature: str, message: str, address: str):
        """
        Verify the authenticity of a "hello" message signature and validate the nonce.

        :param signature: The signed "hello" message.
        :param message: The original "hello" message (e.g., "hello:<nonce>").
        :param address: The Ethereum address expected to have signed the message.
        :return: True if the signature and nonce are valid, False otherwise.
        """
        try:
            # Extract the nonce from the message
            if not message.startswith("hello:"):
                raise ValueError("Invalid message format.")

            # Verify the signature
            message_hash = encode_defunct(text=message)
            recovered_address = Account.recover_message(message_hash, signature=signature)

            # Check if the recovered address matches the expected address
            if recovered_address.lower() != address.lower():
                print("Signature verification failed.")
                return False

            return True

        except Exception as e:
            print(f"Verification error: {e}")
            return False