from flask import Flask, request, redirect
import urllib.parse
from asgiref.wsgi import WsgiToAsgi # type: ignore

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to=vishwanath072005@gmail.com&su={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

    return redirect(gmail_url)

if __name__ == '__main__':
    app.run(debug=True)
