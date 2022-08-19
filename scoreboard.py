from turtle import Turtle

HIGH_SCORE_FILE = 'high_score.txt'


def get_high_score():
    with open(HIGH_SCORE_FILE) as file:
        content = file.read()
        return int(content)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.goto(0, 270)
        self.score = 0
        self.high_score = get_high_score()
        self.color('white')
        self.write_score()

    def write_score(self):
        self.write(f'score: {self.score} high score: {self.high_score}')

    def add_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_FILE, mode='w') as file:
                file.write(f"{self.high_score}")

    def game_over(self):
        self.save_high_score()
        self.home()
        self.write('Game Over')
