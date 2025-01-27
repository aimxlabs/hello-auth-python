# Hello-Message Python SDK

The Hello-Message Python SDK provides a simple interface for generating and verifying "hello" authentication messages for AI-to-AI and AI-to-AI-first services. This SDK is designed to work by using cryptographic signatures for secure authentication.

---

## Installation

Install the SDK from PyPI using pip:

```bash
pip install hello-message-sdk
```

---

## Features

- **Generate Hello Messages**: Create signed "hello" messages using Ethereum private keys.
- **Verify Signatures**: Validate the authenticity of signed "hello" messages.

---

## Quick Start

### Generate and use a "Hello" Message

```python
# Initialize the Hello SDK with your private key
# This private key is for verification purposes only -- should not be used in production
def key_provider():
    # E.g. should retrieve from environment or secure vault, not hardcoded like it is here.
    private_key = '0x4c0883a6910395b1e8dcd7db363c124593f3e8e62e4a8c32ef45b3ef82317b03'  # Replace with your actual private key
    return private_key

hello = Hello(key_provider)

# Generate a signed message
signed_message = hello.generate_hello_message()

# Define the URL of the protected route
url = 'API_ENDPOINT_URL'  # Adjust the URL if your Flask service is hosted elsewhere

# Set up the headers with the signed message for authentication
headers = {
    'X-Hello-Message': signed_message
}

response = requests.get(url, headers=headers)
```

### Verify a "Hello" Message

```python
from hello_message import Hello

message = request.headers.get('X-Hello-Message')

# Verify the signed message
validation_response = Hello.verify_signature(message):
print("Is valid:", validation_response["valid"])

# If the message is valid, you should use the nonce to check if it has already been used to prevent replay attacks
print("Nonce to check:", validation_response["nonce"])
```

---

## API Reference

### Class: `Hello`

#### **`Hello(key_provider: callable)`**

Initialize the Hello object with an Ethereum private key provider.

- `key_provider`: Ethereum private key provider to use retrieve the private key for signing messages.

#### **`get_address() -> str`**

Get the Ethereum address corresponding to the private key.

#### **`generate_hello_message() -> dict`**

Generate a signed "hello" message.

#### **`verify_signature(signature: str, message: str, address: str) -> bool`**

Verify the authenticity of a "hello" message signature.

- `signature`: The signed "hello" message (string).
- `message`: The message to verify (string).
- `address`: The Ethereum address expected to have signed the message (string).

Returns:

- `True` if the signature is valid.
- `False` otherwise.

---

## Testing

Run the tests using `pytest`:

```bash
python -m pytest
```

---

## Contributing

We welcome contributions from the community! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

- [Discussions](https://github.com/aimxlabs/hello-message-python/discussions): Join the conversation.
- [Issues](https://github.com/aimxlabs/hello-message-python/issues): Report bugs or request features.

---

Happy coding with Hello-Message Python SDK!
