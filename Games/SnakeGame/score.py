from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()

        with open('highScoreDeets.txt') as data:            # reading from the file to get the current highscore
            self.high_score = int(data.read())

        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Courier", 15, "normal"))

    def high_score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open('highScoreDeets.txt', mode='w') as data:      # modifying the high score and writing into the file.
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))
