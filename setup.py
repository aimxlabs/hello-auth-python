from setuptools import setup, find_packages

setup(
    name="hello-message",
    version="0.1.0",
    description="A Python package for generating and verifying 'hello' authentication messages, primarily used for authenticating autonomous agents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Garett Rogers",
    author_email="garett@aimx.com",
    url="https://github.com/aimxlabs/hello-message-python",
    packages=find_packages(),
    install_requires=[
        "eth-account>=0.5.7",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
