from logic.base import BaseAI

GROWING_STATE = 'growth'
MATURE_STATE = 'mature'


class FieldAI(BaseAI):

    def progress(self):
        self.age += 1
        if not {MATURE_STATE, GROWING_STATE} & self.states:
            self.states.add(GROWING_STATE)

        if GROWING_STATE in self.states and self.age > 3:
            self.states.remove(GROWING_STATE)
            self.states.add(MATURE_STATE)
