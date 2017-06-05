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
        spare = False
        score = 0
        for game_set in self.score_board:
            if len(game_set) < 1:
                break
            if spare:
                score += game_set[0]
                spare = False
            if len(game_set) < 2:
                continue
            if sum(game_set) == 10:
                spare = True
            score += sum(game_set)
        return score
