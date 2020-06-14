from flask import Flask, render_template, request, flash, jsonify, json
from watering_controller import app, wc

@app.route('/')
@app.route('/index')
def index():
    print(type(wc))
    return render_template('index.html')

@app.route('/edit_programs')
def edit_programs():
    print(type(wc))
    return render_template('edit_programs.html')

@app.route('/change_control_mode', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['control_mode']
    print(jsdata)
    return jsdata

'''
def save_data(data, path=DATA_FILE_PATH):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return
''' 