from flask import Flask, request, jsonify
from hello_message import Hello

app = Flask(__name__)

# Nonces should actually be stored in a database...
used_nonces = []

def require_authentication(f):
    def decorated_function(*args, **kwargs):
        try:
            verification_result = Hello.verify_signature(request.headers.get('X-Hello-Message'))
            
            # Check if the signature is valid
            if not verification_result["valid"]:
                return jsonify({'error': 'Invalid or expired token'}), 401

            # Check if the nonce has already been used - this should query a database
            if verification_result["nonce"] in used_nonces:
                return jsonify({'error': 'Nonce already used'}), 401

            # Add the nonce to the list of used nonces -- this should get stored in a database
            used_nonces.append(verification_result["nonce"])
            
            return f(*args, **kwargs, verification_result=verification_result)
            
        except Exception as e:
            return jsonify({'error': str(e)}), 401

    return decorated_function

@app.route('/protected')
@require_authentication
def protected(verification_result):
    return 'Nice to meet you ' + verification_result["address"]

if __name__ == '__main__':
    app.run(debug=True)
