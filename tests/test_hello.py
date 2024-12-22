import pytest
from hello_message import Hello

# Test the hello message.  
def key_provider():
    # This private key is for verification purposes only -- should not be used in production
    # E.g. should retrieve from environment or secure vault, not hardcoded like it is here.
    private_key = '0x4c0883a6910395b1e8dcd7db363c124593f3e8e62e4a8c32ef45b3ef82317b03'  # Replace with your actual private key
    return private_key

# Initialize the Hello SDK with your private key provider
hello = Hello(key_provider)

def test_hello():
    hello_message = hello.generate_hello_message()
    assert hello.verify_signature(hello_message)["valid"] is True

def test_hello_expired():
    hello_message = hello.generate_hello_message(expires_in_seconds=0)
    assert hello.verify_signature(hello_message)["valid"] is False