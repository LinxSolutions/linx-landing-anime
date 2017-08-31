from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/anime')
def anime():
    return render_template('index.html')


@app.route('/')
def index():
    return redirect('anime')


if __name__ == '__main__':
    app.run(debug=True)