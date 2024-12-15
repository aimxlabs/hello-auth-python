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

    def get_signature(self) -> str:
        """
        Generate a signed "hello" message.

        :return: The signature of the "hello" message in hex format.
        """
        message = encode_defunct(text="hello")
        signed_message = Account.sign_message(message, private_key=self.private_key)
        return signed_message.signature.hex()

    @staticmethod
    def verify_signature(signature: str, address: str) -> bool:
        """
        Verify a signed "hello" message.

        :param signature: The signature of the "hello" message.
        :param address: The Ethereum address that allegedly signed the message.
        :return: True if the signature is valid, False otherwise.
        """
        message = encode_defunct(text="hello")
        recovered_address = Account.recover_message(message, signature=signature)
        return recovered_address.lower() == address.lower()
