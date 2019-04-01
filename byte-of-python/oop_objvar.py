#coding=UTF-8

class Robot:
    """表示一个带有名字的机器人"""
    #class variable
    population = 0

    def __init__(self, name):
        self.name = name
        print("(initializing {})".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("there are still {:d} robot working".format(self.population))

    def say_hi(self):
        """机器人的问候"""
        print("greetings, my master call me {}".format(self.name))

    @classmethod  #how_many = classmethod(how_many)
    def how_many(cls):
        print("we have {:d} robot.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nrobot can do some work here.\n")

print("destroy")
droid1.die()
droid2.die()

Robot.how_many()
