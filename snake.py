from turtle import Turtle

class Snake:
    def __init__(self):
        """Initializes the snake with three segments and sets the head."""
        self.turtles = []  # List to hold all segments of the snake
        self.positions = ((-20, 0), (0, 0), (20, 0))  # Initial positions for the segments
        self.create_snake()
        self.head = self.turtles[-1]  # The head is the last segment created

    def create_snake(self):
        """Creates the initial snake body based on predefined positions."""
        for position in self.positions:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.turtles.append(new_turtle)

    def extend(self):
        """Adds a new segment to the snake at the current tail position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.turtles.insert(0, new_segment)

    def move(self):
        """Moves the snake forward by updating each segment's position."""
        for i in range(len(self.turtles) - 1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.forward(20)

    def up(self):
        """Changes the snake's direction to up if not currently moving down."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Changes the snake's direction to down if not currently moving up."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        """Changes the snake's direction to right if not currently moving left."""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        """Changes the snake's direction to left if not currently moving right."""
        if self.head.heading() != 0:
            self.head.setheading(180)