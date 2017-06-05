class Game(object):
    def __init__(self):
        self._last_frame_was_spare = False
        self.score_board = [[]]

    def record_roll(self, num_pins_knocked):
        last_frame = self.score_board[-1]
        if len(last_frame) < 2:
            last_frame.append(num_pins_knocked)
        elif len(last_frame) == 2:
            self.score_board.append([num_pins_knocked])

    def get_score(self):
        score = 0
        for frame in self.score_board:
            if len(frame) < 1:
                break
            score += self.get_frame_score(frame=frame)
        return score

    def get_frame_score(self, frame):
        frame_score = 0
        if self._last_frame_was_spare:
            frame_score += frame[0]
        if len(frame) < 2:
            return frame_score
        if sum(frame) == 10:
            self._last_frame_was_spare = True
        frame_score += sum(frame)
        return frame_score
