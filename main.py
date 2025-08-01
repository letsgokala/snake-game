from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreturtle import Score

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.change_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() > 290:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            game_is_on = False
            score.game_over()


    

    

    
    
    











screen.exitonclick()