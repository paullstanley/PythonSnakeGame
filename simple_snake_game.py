# Import the Turtle Graphics module
import turtle
import random
# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 200
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"


def game_loop():
    stamper.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < -WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < -HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # Add new head to snake body
        snake.append(new_head)

        # Check for food collision
        if not food_collision():
            # Remove the last segnment of snake.
            snake.pop(0)  # Keep the snake the same length unless fed.

        # Draw the snake for the first time.
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f"Snake Game. Score: {score}")
        screen.update()
        turtle.ontimer(game_loop, DELAY)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorom
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


# Create a window where we will do our drawing.
screen = turtle.Screen()
# Set the dimensions of the Turtle Graphics window.
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

# Event Handlers
screen.listen()
bind_direction_keys()

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color()
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()


# Set snake in motion
reset()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
