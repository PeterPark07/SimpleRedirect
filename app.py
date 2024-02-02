from flask import Flask, redirect, request

app = Flask(__name__)
stored_url = None

@app.route('/set', methods=['GET', 'POST'])
def set_url():
    global stored_url
    if request.method == 'POST':
        url = request.form['url']
        stored_url = url
        return redirect('/')
    return '''
    <form method="post">
        <label for="url">Enter URL:</label>
        <input type="text" id="url" name="url" value="https://"required>
        <button type="submit">Set URL</button>
    </form>
'''

@app.route('/')
def redirect_to_url():
    global stored_url
    if stored_url:
        return redirect(stored_url, code=302)
    else:
        return 'No redirect SET yet.'

if __name__ == '__main__':
    app.run(debug=True)
