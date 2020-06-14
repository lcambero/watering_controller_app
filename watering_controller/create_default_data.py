import json

CONFIG_FILE_PATH = 'config.json'
DATA_FILE_PATH = 'data.json'

with open(CONFIG_FILE_PATH) as f:
    config = json.load(f)

data = {}
data['control_mode'] = 'manual'
data['programs'] = []
data['circuits'] = []

for i in range(config['n_programs']):
    new_program = {
            'id': i,
            'selected': False,
            'activated': False,
            'days': [],
            'start_hour': 0,
            'start_minute': 0,
            'circuit_ids': [],
            'time_per_circuit_mins': 0
        }
    data['programs'].append(new_program)

for i in range(config['n_circuits']):
    new_circuit = {
            'id': i,
            'activated': False
        }
    data['circuits'].append(new_circuit)

with open(DATA_FILE_PATH, 'w') as outfile:
    json.dump(data, outfile)