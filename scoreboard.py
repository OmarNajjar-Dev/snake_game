from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """Initializes the scoreboard at the top of the screen."""
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0, 300)  # Position the scoreboard at the top center
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Displays the current score on the screen."""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increases the score by 1 and updates the display."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Displays the Game Over message and final score."""
        self.screen.bgcolor("darkred")
        self.home()  # Move the turtle to the center
        self.write(f"Game Over\nFinal Score: {self.score}", align="center", font=("Arial", 24, "normal"))