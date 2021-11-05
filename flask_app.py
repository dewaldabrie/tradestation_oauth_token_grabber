from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def capture_auth_code():
    auth_code = request.args.get('code')
    with open('auth_code.txt', mode='w') as fh:
        fh.write(auth_code)
    return f"<pre>{auth_code}</pre>"