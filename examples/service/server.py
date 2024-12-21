from flask import Flask, request, jsonify
from hello_message import Hello

app = Flask(__name__)

# Nonces should actually be stored in a database...
used_nonces = []

def require_authentication(f):
    def decorated_function(*args, **kwargs):
        signature = request.headers.get('X-Hello-Signature')
        message = request.headers.get('X-Hello-Message')
        address = request.headers.get('X-Hello-Address')

        # Check if the nonce has not been used before
        if message.split(':')[1] in used_nonces:
            return jsonify({'error': 'Nonce already used'}), 401

        try:
            # Verify the signed message
            if not Hello.verify_signature(signature, message, address):
                return jsonify({'error': 'Invalid or expired token'}), 401

            print('Hello', address)

            used_nonces.append(message.split(':')[1])
        except Exception as e:
            return jsonify({'error': str(e)}), 401

        return f(*args, **kwargs)
    return decorated_function

@app.route('/protected')
@require_authentication
def protected():
    print('SUCCESS: Protected route has been accessed')
    return 'This is a protected route.'

if __name__ == '__main__':
    app.run(debug=True)
