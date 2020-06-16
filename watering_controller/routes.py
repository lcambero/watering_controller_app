from flask import Flask, render_template, request, flash, jsonify, json
from watering_controller import app, wc

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/control_mode', methods=['GET'])
def get_control_mode():
    return jsonify({'control_mode': wc.control_mode})

@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify(
        {'n_programs': wc.n_programs, 
         'programs': [program.to_dict() for program in wc.programs]})

@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):

    return jsonify({'program_id': program_id}) 

@app.route('/programs', methods=['POST'])
def post_programs():
    return jsonify()

@app.route('/edit_programs')
def edit_programs():
    return render_template('edit_programs.html')


@app.route('/change_control_mode', methods=['POST'])
def get_post_javascript_data():
    jsdata = request.get_json()
    print(jsdata)
    print(type(jsdata))
    return jsdata
