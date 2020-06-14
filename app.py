from watering_controller import app, wc
#from watering_controller.controller import WateringController
import json

CONFIG_FILE_PATH = 'config.json'
DATA_FILE_PATH = 'data.json'

if __name__ == '__main__':
    with open(CONFIG_FILE_PATH) as f:
        config = json.load(f)
    with open(DATA_FILE_PATH) as f:
        data = json.load(f)

    if config['n_programs'] != len(data['programs']) or config['n_circuits'] != len(data['circuits']):
        raise Exception('Config and data have different number of programs/circuits')
    else:
        #global wc 
        #wc = WateringController(data)
        pass

    app.run(host='0.0.0.0', port=3000, debug=True)