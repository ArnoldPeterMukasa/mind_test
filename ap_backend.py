from flask import Flask, render_template, redirect, url_for 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/yes')
def yes():
    return render_template('yes_page.html')

@app.route('/exit')
def exit(): #will shutdown the flask development server
    # return render_template('no_page.html')
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return 'server is not running with the Werkzeug Server'
    func()
    return 'Server shutting down....'

if __name__ == '__main__':
    app.run(debug=True, port=5000)