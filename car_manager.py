from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            random_y = random.randint(-250, 250)
            # new_car.shape("turtle")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def car_move(self):
        for item in self.all_cars:
            item.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
