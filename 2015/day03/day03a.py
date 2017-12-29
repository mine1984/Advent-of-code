# Santa is delivering presents to an infinite two-dimensional grid of houses.
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
#
# Santa ends up visiting some houses more than once. How many houses receive at least one present?

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
directions = input()
houses = [(santa.x,santa.y)]
counter = 1
for direct in directions:
    santa.move(direct)
    x = santa.x
    y = santa.y
    if (x,y) not in houses:
        houses.append((x,y))
        counter += 1
print(counter)
