class State:
    def __init__(self, unit1, unit2, unit3):
        self.unit1 = unit1
        self.unit2 = unit2
        self.unit3 = unit3
        self.description = "class for sorting and returning unit states"

    def get_state_list(self):
        return [self.unit1, self.unit2, self.unit3]

    def get_unit1(self):
        return self.unit1

    def get_unit2(self):
        return self.unit2

    def get_unit3(self):
        return self.unit3

    def set_unit1(self, state):
        self.unit1 = state

    def set_unit2(self, state):
        self.unit2 = state

    def set_unit3(self, state):
        self.unit3 = state

