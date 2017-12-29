# Santa is delivering presents to an infinite two-dimensional grid of houses.
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
#
# Santa ends up visiting some houses more than once. How many houses receive at least one present?
#
# Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?

class player:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self,direct):
        if direct == '^':
            self.y += 1
        if direct == 'v':
            self.y += -1
        if direct == '>':
            self.x += 1
        if direct == '<':
            self.x += -1

santa = player()
robot = player()

directions = input()
houses = [(santa.x,santa.y)]
counter = 1
steps = int(len(directions)/2)
for i in range(steps):
    santa.move(directions[i*2])
    robot.move(directions[i*2+1])
    x_s = santa.x
    y_s = santa.y
    x_r = robot.x
    y_r = robot.y
    if (x_s,y_s) not in houses:
        houses.append((x_s,y_s))
        counter += 1
    if (x_r,y_r) not in houses:
        houses.append((x_r,y_r))
        counter += 1
print(counter)
