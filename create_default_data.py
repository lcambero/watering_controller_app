import json

CONFIG_FILE_PATH = 'config.json'

N_PROGRAMS = 3
N_CIRCUITS = 12

config = {}
config['programs'] = []
config['circuits'] = []

for i in range(N_PROGRAMS):
    new_program = {
            'id': i + 1,
            'selected': False,
            'days': [],
            'start_hour': 0,
            'start_minute': 0,
            'circuit_ids': [],
            'time_per_circuit_mins': 0
        }
    config['programs'].append(new_program)

for i in range(N_CIRCUITS):
    new_circuit = {
            'id': i + 1,
            'pin': 0
        }
    config['circuits'].append(new_circuit)

with open(CONFIG_FILE_PATH, 'w') as outfile:
    json.dump(config, outfile)