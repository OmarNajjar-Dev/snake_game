from turtle import Screen
from snake import Snake
from food import Food
from time import sleep
from scoreboard import Scoreboard

# Setup the game window
window = Screen()
window.title("Snake Game")
window.setup(width=800, height=700)
window.bgcolor("darkcyan")
window.tracer(0)

# Initialize game objects
snake = Snake()
natural_food = Food(color="red")
magic_food = Food(color="darkgreen")
magic_food.hideturtle()  # Hide magic food initially
score = Scoreboard()

# Game variables
red_food_eat = 0  # Counts how many natural food items have been eaten
helper = 0  # To slow down the game

# Global variable to manage the game loop
game_on = True

# Handle window close event safely
def safe_close():
    global game_on
    game_on = False  # Stop the game loop
    try:
        window.bye()  # Close the Turtle graphics window safely
    except:
        pass

# Bind the close event to the safe_close function
window._root.protocol("WM_DELETE_WINDOW", safe_close)

# Main game loop
def run_game(red_food_eat, helper): 
    global game_on
    while game_on:
        # Move the snake and update the screen
        snake.move()
        window.update()
        sleep(0.1 - min(0.09, (score.score - helper) * 0.005))
        
        # Listen for key presses to control the snake
        window.listen()
        window.onkey(snake.up, "Up")
        window.onkey(snake.down, "Down")
        window.onkey(snake.right, "Right")
        window.onkey(snake.left, "Left")

        # Check if the snake eats natural food
        if snake.head.distance(natural_food) < 15:
            natural_food.appear()
            snake.extend()
            score.increase_score()
            red_food_eat += 1
            # Make magic food appear every 3 natural food items eaten
            if not magic_food.isvisible() and red_food_eat % 3 == 0:
                magic_food.appear()
                magic_food.showturtle()

        # Check if the snake eats magic food
        if magic_food.isvisible() and snake.head.distance(magic_food) < 15:
            magic_food.hideturtle()
            snake.extend()
            score.increase_score()
            helper += 2  # Reduce difficulty after eating magic food

        # Check if the snake collides with the wall
        if snake.head.xcor() >= 380 or snake.head.xcor() <= -380 or abs(snake.head.ycor()) > 320:
            game_on = False
            score.game_over()

        # Check if the snake collides with its own body
        for segment in snake.turtles[:-1]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()


# Start the game
if __name__ == "__main__":
    try:
        sleep(1)
        run_game(red_food_eat, helper)
    except:
        pass

# Close the game window when clicked
try:
    window.exitonclick()
except:
    pass