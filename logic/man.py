from logic.base import BaseAI

MOVE_L = 'move_left'
MOVE_R = 'move_right'
MOVE_U = 'move_up'
MOVE_D = 'move_down'
BUILD_FIELD = 'build_field'

MOVES = {MOVE_L, MOVE_R, MOVE_U, MOVE_D}


class ManAI(BaseAI):

    def __init__(self):  # just for keyboard control
        super(ManAI, self).__init__()
        self.next_state = None

    def progress(self):
        self.age += 1
        self.states -= MOVES

        for need in self.needs:
            self.current_needs[need] += self.needs[need]

        if BUILD_FIELD in self.states:
            self.states.remove(BUILD_FIELD)

        if self.next_state:  # just for keyboard control
            self.states.add(self.next_state)
            self.next_state = None
