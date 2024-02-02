from flask import Flask, redirect
from urllib.parse import quote

app = Flask(__name__)
stored_url = None

@app.route('/<path:encoded_url>')
def set_url(encoded_url):
    global stored_url
    stored_url = quote(encoded_url)
    return f'Successfully set URL to: {encoded_url}'

@app.route('/')
def redirect_to_url():
    global stored_url
    if stored_url:
        return redirect(stored_url, code=302)
    else:
        return 'No URL set yet.'

if __name__ == '__main__':
    app.run(debug=True)
