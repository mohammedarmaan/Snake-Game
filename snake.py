from turtle import Turtle

# constants
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 10
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # creating segments of a snake and placing them beside each-other
    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.pu()
        segment.goto(position)
        self.snake.append(segment)

    # Increasing snake's length
    def extend(self):
        self.add_segment(self.snake[-1].position())
    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.fd(MOVE_DIST)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
