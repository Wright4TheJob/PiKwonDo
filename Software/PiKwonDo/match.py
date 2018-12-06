"""Match instance class for passing between game controller and GUI."""


class Match():
    """A particular match driven by the rules of TaeKwonDo."""

    def __init__(self):
        """Begin a new match."""
        # print('Started new match!')
        self.red_score = 0
        self.blue_score = 0
        self.red_penalties = 0
        self.blue_penalties = 0
        self.current_section = 1
