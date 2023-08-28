from turtle import Turtle
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_dis = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in starting_pos:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_dis)

    def up(self):
        if self.head.heading() != down:
            self.segments[0].setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.segments[0].setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.segments[0].setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.segments[0].setheading(right)