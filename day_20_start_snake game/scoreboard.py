from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as first_file:
            content = first_file.read()
        
        self.high_score = int(content)
        
        


        
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE = {self.score}           Highscore:{self.high_score} ', move=False, align='center', font=('Courier', 15, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align='center', font=('Courier', 20,'normal'))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score +=100
        self.update_scoreboard()


