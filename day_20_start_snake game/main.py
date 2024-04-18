from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import pygame


pygame.mixer.init()



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("EFE'S SNAKE GAME")
screen.tracer(0)



def play_sound(sound, loops=0):
    if isinstance(sound, pygame.mixer.Sound):
        sound.play(loops=loops)
    elif isinstance(sound, str):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(loops=loops)

game_is_on = True
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# play_sound(theme_song, loops=-1)

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        # play_sound(food_sound)
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if (
        snake.head.xcor() > 290 or snake.head.xcor() < -290 or
        snake.head.ycor() > 290 or snake.head.ycor() < -290
    ):
        
        score_board.reset()
        snake.reset()

    for segment in snake.snake_obj[1:]:
        if snake.head.distance(segment) < 2:
            
            score_board.reset()
            snake.reset()

screen.exitonclick()
