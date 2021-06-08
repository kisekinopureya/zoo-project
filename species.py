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
        if random.choice([True,False]) == True:
            self.x += self.movement
            if self.x > 500:
                self.x -= self.movement
        else:
            self.x -= self.movement
            if self.x < 0:
                self.x += self.movement

        if random.choice([True,False]) == True:
            self.y += self.movement
            if self.y > 500:
                self.y -= self.movement
        else:
            self.y -= self.movement
            if self.y < 0:
                self.y += self.movement
            
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

