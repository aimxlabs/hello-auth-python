from setuptools import setup, find_packages

setup(
    name="hello-message-sdk",
    version="0.1.0",
    description="A Python SDK for AI agents to securely generate and verify 'hello' authentication messages, enabling seamless interaction between AI agents and AI-centric services.",
    long_description=open("README.md", encoding="utf-8").read(),  # Ensure correct encoding for non-ASCII characters
    long_description_content_type="text/markdown",
    author="Garett Rogers",
    author_email="garett@aimx.com",
    url="https://github.com/aimxlabs/hello-message-python",
    packages=find_packages(include=["hello_message", "hello_message.*"]),  # Explicitly include the package
    install_requires=[
        "eth-account>=0.13.4",
    ],
    extras_require={  # Allow optional dependencies for additional features
        "dev": ["pytest"],  # Development tools
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="hello-message, authentication, ethereum, sdk, ai, artificial-intelligence, autonomous-agents, ai-first-services, blockchain, ai-authentication",
    python_requires=">=3.6"
)
