#!/usr/bin/env_python3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        twitter_id = request.form['twitter_id']
        return render_template('result.html', twitter_id=twitter_id)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

