import pytest
from hello_message import Hello

def test_hello():
    private_key = "0x4c0883a6910395b1e8dcd7db363c124593f3e8e62e4a8c32ef45b3ef82317b03"
    hello = Hello(private_key)
    hello_message = hello.generate_hello_message()
    address = hello.get_address()
    assert hello.verify_signature(hello_message["signature"], hello_message["message"], address) is True