import requests
import time
from hello_message import Hello

# Initialize the Hello SDK with your private key
# This private key is for verification purposes only -- should not be used in production
def key_provider():
    # E.g. should retrieve from environment or secure vault, not hardcoded like it is here.
    private_key = '0x4c0883a6910395b1e8dcd7db363c124593f3e8e62e4a8c32ef45b3ef82317b03'  # Replace with your actual private key
    return private_key

hello = Hello(key_provider)

# Define the URL of the protected route
url = 'http://127.0.0.1:5000/protected'  # Adjust the URL if your Flask service is hosted elsewhere

# Set up the headers with the signed message for authentication
headers = {
    'X-Hello-Message': hello.generate_hello_message(),
}

try:
    # Make a GET request to the protected route
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print('SUCCESS:', response.text)
        #print(response.text)
    else:
        print('ERROR:', response.text)

    # Simulated replay attack
    replay_attack_response = requests.get(url, headers=headers)

    # Check if the request was successful
    if replay_attack_response.status_code >= 400:
        print('SUCCESS: Replay attack blocked (this is good)', replay_attack_response.text)
    else:
        print(f'ERROR: Replay attack was succesful (this is bad).')    
    

except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
