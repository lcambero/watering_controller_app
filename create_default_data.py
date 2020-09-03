import json

CONFIG_FILE_PATH = 'data.json'

N_PROGRAMS = 3
N_CIRCUITS = 12

config = {}
config['programs'] = []
config['circuits'] = []

for i in range(N_PROGRAMS):
    new_program = {
            'id': i + 1,
            'selected': False,
            'days': {d: False for d in ['L', 'M', 'X', 'J', 'V', 'S', 'D']},
            'starts': {s + 1: {'hour': '00:00', 'activated': False} for s in range(3)},
            'circuits': {c + 1: {'time': 0, 'activated': False} for c in range(N_CIRCUITS)}
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