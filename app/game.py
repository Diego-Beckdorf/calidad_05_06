class Game(object):
    def __init__(self):
        self._last_set_was_spare = False
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
        for game_set in self.score_board:
            if len(game_set) < 1:
                break
            set_score = self.get_set_score(game_set=game_set)
            score += set_score
        return score

    def get_set_score(self, game_set):
        set_score = 0
        if self._last_set_was_spare:
            set_score += game_set[0]
        if len(game_set) < 2:
            return set_score
        if sum(game_set) == 10:
            self._last_set_was_spare = True
        set_score += sum(game_set)
        return set_score
