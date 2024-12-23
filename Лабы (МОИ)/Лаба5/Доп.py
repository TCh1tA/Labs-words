class Square():
    def __init__(self, side):
        self.side = side

    def get_square(self):
        self.side = self.side ** 2

    def get_side(self):
        return self.side

