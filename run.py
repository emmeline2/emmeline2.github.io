from flask import Flask, g, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/resume')
def adopt():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
