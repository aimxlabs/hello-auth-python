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

# Generate a signed message
signed_message = hello.generate_hello_message()

# Define the URL of the protected route
url = 'http://127.0.0.1:5000/protected'  # Adjust the URL if your Flask service is hosted elsewhere

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

# you should check if nonce has already been used here to prevent replay attacks

# Verify the signed message
validation_response = Hello.verify_signature(message):
print("Is valid:", validation_response["is_valid"])
```

---

## API Reference

### Class: `Hello`

#### **`Hello(private_key: str)`**

Initialize the Hello object with an Ethereum private key.

- `private_key`: Ethereum private key (string) used for signing messages.

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
