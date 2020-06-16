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
        assert(all([type(val) == int for val in [program[x] for x in ['id', 'start_hour', 'start_minute', 'time_per_circuit_mins']]]))
        assert(all([type(val) == list for val in [program[x] for x in ['days', 'circuit_ids']]]))
        assert(type(program['selected']) == bool)

        self.id = program['id']
        self.selected = program['selected']
        self.days = program['days']
        self.start_hour = program['start_hour']
        self.start_minute = program['start_minute']
        self.circuit_ids = program['circuit_ids']
        self.time_per_circuit_mins = program['time_per_circuit_mins']
        self.activated = False

        return

    def to_dict(self):
        dict_program = {}

        dict_program['id'] = self.id
        dict_program['selected'] = self.selected
        dict_program['days'] = self.days
        dict_program['start_hour'] = self.start_hour
        dict_program['start_minute'] = self.start_minute
        dict_program['circuit_ids'] = self.circuit_ids
        dict_program['time_per_circuit_mins'] = self.time_per_circuit_mins
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