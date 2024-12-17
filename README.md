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

### Generate a "Hello" Message

```python
from hello_message import Hello

# Initialize the Hello SDK with a private key
private_key = "<your_ethereum_private_key>"
hello = Hello(private_key=private_key)

# Get the Ethereum address
address = hello.get_address()
print("Address:", address)

# Generate a signed "hello" message
signature = hello.get_signature()
print("Signature:", signature)
```

### Verify a "Hello" Message

```python
from hello_message import Hello

# Example signature and address
signature = "<signature_from_hello_message>"
address = "<ethereum_address>"

# Verify the signature
is_valid = Hello.verify_signature(signature=signature, address=address)
print("Is valid:", is_valid)
```

---

## API Reference

### Class: `Hello`

#### **`Hello(private_key: str)`**

Initialize the Hello object with an Ethereum private key.

- `private_key`: Ethereum private key (string) used for signing messages.

#### **`get_address() -> str`**

Get the Ethereum address corresponding to the private key.

#### **`get_signature() -> str`**

Generate a signed "hello" message.

#### **`verify_signature(signature: str, address: str) -> bool`**

Verify the authenticity of a "hello" message signature.

- `signature`: The signed "hello" message (string).
- `address`: The Ethereum address expected to have signed the message (string).

Returns:

- `True` if the signature is valid.
- `False` otherwise.

---

## Testing

Run the tests using `pytest`:

```bash
pytest tests/
```

---

## Contributing

We welcome contributions from the community! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

- [Discussions](https://github.com/aimxlabs/hello-message-python/discussions): Join the conversation.
- [Issues](https://github.com/aimxlabs/hello-message-python/issues): Report bugs or request features.
- [Documentation](https://github.com/aimxlabs/hello-message-python/docs): Learn more about the SDK.

---

Happy coding with Hello-Message Python SDK!
