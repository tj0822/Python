# class Ball:
#
#     def __init__(self, color, size, direction):
#         self.color = color
#         self.size = size
#         self.direction = direction
#
#     def __str__(self):
#         msg = "Hi, I'm a " + self.size + " " + self.color + " ball"
#         return msg
#
#     # def bounce(self):
#     #     if self.direction == "down":
#     #         self.direction = "up"
#
# myBall = Ball("red", "small", "down")
# print myBall

# myBall.direction = "down"
# myBall.color = "green"
# myBall.size = "small"

# print "I just created a ball."
# print "My ball is", myBall.size
# print "My ball is", myBall.color
# print "My ball's direction is", myBall.direction
# print
# myBall.bounce()
# print "Now the ball's direction is", myBall.direction







class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with "
            for condiment in self.condiments:
                msg = msg + condiment + ", "
        msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"

    def addCondiment(self, condiment):
        self.condiments.append(condiment)

myDog = HotDog()
print myDog.cooked_level
print myDog.cooked_string
print myDog.condiments


print "Now I'm going to cook the hot dog"
myDog.cook(4)
print myDog.cooked_level
print myDog.cooked_string

print myDog
print "Cooking hot dog for 3 more minutes..."

myDog.cook(3)
print myDog
print "What happens if I cook it for 10 more minutes?"
myDog.cook(10)
print myDog
print "Now, I'm going to add some stuff on my hot dog"
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")

print myDog