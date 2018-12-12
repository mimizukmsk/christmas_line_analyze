#!/usr/bin/env_python3

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import split_each_weeks_by_txt_3 as split_each_weeks_by_txt_3

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENTION = 'txt'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    # key_word = request.files['txt_file']
    e_personality, number_of_weekss = split_each_weeks_by_txt_3.main()
    values_a = []
    if request.method == 'POST':
        for e_p in e_personality:
            e_p = e_p * 100
            values_a.append(e_p)
        labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #values_a = [10, 50 , 100, 35, 86, 72]
        return render_template('result.html', labels=labels, values_a=values_a)
    else:
        return redirect(url_for('index'))

@app.route('/upload/<filenames>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

