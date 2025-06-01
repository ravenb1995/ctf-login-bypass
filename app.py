
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return open('login.html').read()

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pwd = request.form['password']
    if user == "admin" and ("'1'='1" in pwd or "1' or '1" in pwd):
        return "<h1>Welcome, admin!</h1><p>Flag: CTF{SQL_BYPASS_SUCCESS}</p>"
    else:
        return "<h1>Access Denied</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
