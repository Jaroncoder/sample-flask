from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/another-page')
def another_page():
    return 'This is another page!'

if __name__ == "__main__":
    app.run()
