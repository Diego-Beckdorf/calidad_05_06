class Game(object):
    def __init__(self):
        self.score_board = [[]]

    def record_roll(self, num_pins_knocked):
        last_set = self.score_board[-1]
        if len(last_set) < 2:
            last_set.append(num_pins_knocked)
        elif len(last_set) == 2:
            new_set =[num_pins_knocked]
            self.score_board.append(new_set)

    def get_score(self):
        score = 0
        for set in self.score_board:
            if len(set) == 2:
                score += sum(set)
        return score
