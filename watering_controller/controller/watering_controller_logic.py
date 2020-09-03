class WateringController():
    def __init__(self, config):
        assert(type(config) == dict)

        self.control_mode = 'automatic'

        self.n_programs = len(config['programs'])
        self.n_circuits = len(config['circuits'])

        self.programs = [Program(program) for program in config['programs']]
        self.circuits = [Circuit(circuit) for circuit in config['circuits']]

        return

class Program():
    def __init__(self, program):
        assert(type(program) == dict)
        assert(type(program['id']) == int)
        assert(all([type(val) == dict for val in [program[x] for x in ['days', 'starts', 'circuits']]]))
        assert(type(program['selected']) == bool)

        self.id = program['id']
        self.selected = program['selected']
        self.days = program['days']
        self.starts = program['starts']
        self.circuits = program['circuits']
        self.activated = False

        return

    def to_dict(self):
        dict_program = {}

        dict_program['id'] = self.id
        dict_program['selected'] = self.selected
        dict_program['days'] = self.days
        dict_program['starts'] = self.starts
        dict_program['circuits'] = self.circuits
        dict_program['activated'] = self.activated

        assert(type(dict_program) == dict)
        return dict_program

    def select_program(selected):
        assert(type(selected) == bool)
        self.selected = selected
        return

class Circuit():
    def __init__(self, circuit):
        assert(type(circuit) == dict)
        assert(all([type(val) == int for val in [circuit[x] for x in ['id', 'pin']]]))

        self.id = circuit['id']
        self.pin = circuit['pin']
        self.activated = False

        return


'''
def save_data(data, path=DATA_FILE_PATH):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return
''' 