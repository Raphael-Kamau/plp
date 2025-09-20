from flask import Flask, request, jsonify
from db import save_message

app = Flask(__name__)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'success': False, 'error': 'Missing fields'}), 400

    success = save_message(name, email, message)
    return jsonify({'success': success})

if __name__ == "__main__":
    app.run(debug=True)
