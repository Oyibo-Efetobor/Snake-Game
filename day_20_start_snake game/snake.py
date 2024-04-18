from turtle import Turtle, Screen
import random
import time

screen = Screen()

colors_list = ['red','orange','yellow','green','blue','purple','white']


position = [(0,0), (-20,0), (-40,0)]
game_is_on = True

class Snake:
    def __init__(self):
        counter = 0
        self.snake_obj =[]
        self.speed = 20
        for i in position:
            if counter == 0:
                segment_1 = Turtle('triangle')
                segment_1.color(random.choice(colors_list))
                segment_1.penup()
                segment_1.goto(i)
                self.snake_obj.append(segment_1)
                self.head = self.snake_obj[0]
                counter = 1
            if counter != 0:
                segment_1 = Turtle('square')
                segment_1.color(random.choice(colors_list))
                segment_1.penup()
                segment_1.goto(i)
                self.snake_obj.append(segment_1)
                self.head = self.snake_obj[0]

    def create_snake(self):
        for i in position:
           self.add_segment(i) 
    
    def add_segment(self, position):
        segment_1 = Turtle('square')
        segment_1.color(random.choice(colors_list))
        segment_1.penup()
        segment_1.goto(position)
        self.snake_obj.append(segment_1)
        self.speed += 1


    def extend(self):
        self.add_segment(self.snake_obj[-1].position())
        
    
    def move(self):
        for i in range(len(self.snake_obj) -1, 0, -1):
            new_x = self.snake_obj[i-1].xcor()
            new_y = self.snake_obj[i-1].ycor()
            self.snake_obj[i].goto(new_x,new_y)
            
        self.head.forward(20)

    def up(self):
        if self.snake_obj[0].heading() != 270:
            self.snake_obj[0].setheading(90)
    def down(self):
        if self.snake_obj[0].heading() != 90:
            self.snake_obj[0].setheading(270)
    def left(self):
        if self.snake_obj[0].heading() != 0:
            self.snake_obj[0].setheading(180)
    def right(self):
        if self.snake_obj[0].heading() != 180:
            self.snake_obj[0].setheading(0)

    def reset(self):
        for seg in self.snake_obj:
            seg.goto(1000,1000)
        self.snake_obj.clear()
        self.create_snake()
        self.head = self.snake_obj[0]
        






