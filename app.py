from flask import Flask, redirect

app = Flask(__name__)
stored_url = None

@app.route('/<path:url>')
def set_url(url):
    global stored_url
    stored_url = url
    return f'Successfully set URL to: {url}'

@app.route('/')
def redirect_to_url():
    global stored_url
    if stored_url:
        return redirect(stored_url, code=302)
    else:
        return 'No URL set yet.'

if __name__ == '__main__':
    app.run(debug=True)
