#!/usr/bin/python

import random
from random import randint

species = {
        'Sheep': 0,
        'Cow': 1,
        'HenRooster': 2,
        'Wolf': 3,
        'Lion': 4,
        'Hunter': 5
        }

class Chars:
    def __init__(self):
        self.name = type(self).__name__
        self.x = randint(0,500) #set random coordinates at initialization
        self.y = randint(0,500)
    
    def tick(self):
        #Based on their movement unit, randomly move unit and check if it exceeds the field
        tempx = random.choice([self.movement, -self.movement])
        self.x += tempx
        if self.x > 500 or self.x < 0:
            self.x += 2 * -tempx

        tempy = random.choice([self.movement, -self.movement])
        self.y += tempy
        if self.y > 500 or self.x < 0:
            self.y += 2 * -tempy
            
class Sheep(Chars, object):
    def __init__(self, gender, x, y):
        self.species = species['Sheep']
        self.movement = 2
        self.gender = gender
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        super(Sheep, self).__init__()
        
class Wolf(Chars, object):
    def __init__(self, gender, x, y):
        self.species = species['Wolf']
        self.movement = 3
        self.gender = gender
        self.huntsFor = [ 0, 2 ]
        self.huntRadius = 4
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        super(Wolf, self).__init__()

class Cow(Chars, object):        
    def __init__(self, gender, x, y):
        self.species = species['Cow']
        self.movement = 2
        self.gender = gender
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        super(Cow, self).__init__()

class HenRooster(Chars, object):           #Only difference is gender
    def __init__(self, gender, x, y):
        self.species = species['HenRooster']
        self.movement = 1
        self.gender = gender
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        super(HenRooster, self).__init__()

class Lion(Chars, object):        
    def __init__(self, gender, x, y):
        self.species = species['Lion']
        self.movement = 4
        self.gender = gender
        self.huntsFor = [ 0, 1 ]
        self.huntRadius = 5
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        super(Lion, self).__init__()

class Hunter(Chars, object):        
    def __init__(self, gender, x, y):
        self.species = species['Hunter']
        self.movement = 1
        self.gender = None
        self.huntsFor = [ 0, 1, 2, 3, 4 ]
        self.huntRadius = 8
        super(Hunter, self).__init__()

