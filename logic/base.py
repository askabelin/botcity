class BaseAI(object):

    needs = {}

    def __init__(self):
        self.states = set()
        self.age = 0
        self.current_needs = {k: 0 for k in self.needs}
