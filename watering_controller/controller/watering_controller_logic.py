#!/usr/bin/env python

class WateringController():
    def __init__(self, data={'programs': [], 'circuits': []}):
        assert(type(data) == dict)

        self.n_programs = len(data['programs'])
        self.n_circuits = len(data['circuits'])

        self.programs = [Program() for program in data['programs']]
        self.circuits = [Circuit() for circuit in data['circuits']]

        return

class Program():
    def __init__(self):

        return


class Circuit():
    def __init__(self):
        return


'''

CONFIG_FILE_PATH = 'config.json'
DATA_FILE_PATH = 'data.json'

with open(CONFIG_FILE_PATH) as f:
        config = json.load(f)
    with open(DATA_FILE_PATH) as f:
        data = json.load(f)

    if config['n_programs'] != len(data['programs']) or config['n_circuits'] != len(data['circuits']):
        raise Exception('Config and data have different number of programs/circuits')
    else:
        pass #WateringController(data)


'''