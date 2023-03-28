from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_cars
        
    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.up()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(COLORS[random.randint(0,5)])
            car.goto(310, random.randint(-245,250))
            car.setheading(180)
            self.cars.append(car)
        
    def cars_move(self):
        for car in range(0, (len(self.cars) - 1)):
            self.cars[car].forward(self.speed)
        
    def increase_speed(self):
        self.speed += MOVE_INCREMENT

