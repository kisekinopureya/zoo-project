#!/usr/bin/python

import random, time, sys
from species import Sheep, Cow, HenRooster, Wolf, Lion, Hunter, species

TICK_RATE = 1000
if len(sys.argv) >= 2:
    argv = sys.argv[1]
else:
    argv = ""
start_time = time.time()
idlist = []

class Main:
    def __init__(self):
        self.field = []

        self._add(Sheep, "M", 15, None, None)
        self._add(Sheep, "F", 15, None, None)
        self._add(Cow, "M", 5, None, None)
        self._add(Cow, "F", 5, None, None)
        self._add(HenRooster, "F", 10, None, None)
        self._add(HenRooster, "M", 10, None, None)
        self._add(Wolf, "M", 5, None, None)
        self._add(Wolf, "F", 5, None, None)
        self._add(Lion, "M", 4, None, None)
        self._add(Lion, "F", 4, None, None)
        self._add(Hunter,"N", 1, None, None)

        i = 0
        while i < TICK_RATE:
            self._tick()
            i += 1

        self._count()

    def _tick(self):
        for species in self.field:
            species.tick()
        self._simulate()

    def _add(self, animal, gender, number, x, y):
        for i in range(number):
            self.field += [animal(gender, x, y)]

    def _simulate(self):
        if TICK_RATE % 3 == 0:
            idlist.clear()
        self._hunting()
        self._reproduction()

    def _hunting(self):
        for i in self.field:
            if hasattr(i, "huntsFor"):
                for z in self.field:
                    for g in i.huntsFor:
                        if z.species == g:
                            if ((i.x - i.huntRadius) <= z.x <= (i.x + i.huntRadius)) and ((i.y - i.huntRadius) <= z.y <= (i.y + i.huntRadius)):
                                self.field.remove(z)
                                if argv == "--debug":
                                    print(i.name,"(",i.x,",",i.y,") has hunted", z.name,"(", z.x,",",z.y,")")

    def _reproduction(self):
        for i in self.field:
            for z in self.field:
                if (i.species == z.species and i.gender != z.gender) and (idlist.count(id(i)) == 0 or idlist.count(id(z)) == 0): # to prevent infinite reproduction
                    if ((i.x - 3) <= z.x <= (i.x + 3)) and ((i.y - 3) <= z.y <= (i.y + 3)):
                        functocall = getattr(i, "name") #hacky way to call function
                        if argv == "--debug":
                            print("New ", i.name, "From", "(",i.x, i.y, i.gender, "/", z.x, z.y, z.gender,")")
                        self._add(globals()[functocall], random.choice(['F','M']), 1, (i.x + random.choice([1,-1])), (i.y + random.choice([1,-1])))
                        temp = (id(i),id(z))
                        idlist.extend(temp)
                    
    def _count(self):
        SheepCount, CowCount, HenCount, RoosterCount, WolfCount, LionCount = 0, 0, 0, 0, 0, 0 
        for i in self.field:
            if i.name == "Sheep":
                SheepCount += 1
            if i.name == "Cow":
                CowCount += 1
            if i.name == "HenRooster" and i.gender == "M":
                RoosterCount += 1
            if i.name == "HenRooster" and i.gender == "F":
                HenCount += 1
            if i.name == "Wolf":
                WolfCount += 1
            if i.name == "Lion":
                LionCount += 1
        print(" Sheep Count:", SheepCount,"\n", "Cow Count:", CowCount,"\n",
                "Hen Count:", HenCount,"\n", "Rooster Count:", RoosterCount,"\n",
                "Wolf Count:", WolfCount,"\n", "Lion Count:", LionCount)
        if argv == "--debug":
            print(time.time() - start_time)

if __name__ == '__main__':
    Main()
