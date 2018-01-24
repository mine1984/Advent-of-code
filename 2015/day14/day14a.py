# Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.
# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.
#
# After exactly 2503 seconds, what distance has the winning reindeer traveled?

class Reindeer():

    def __init__(self, name, speed, move_time, rest_time):

        self.name = name
        self.speed = speed
        self.move_time = move_time
        self.rest_time = rest_time

    def find_distance(self, time):

        cycle = self.move_time + self.rest_time
        cycle_dist = (time // cycle) * self.speed * self.move_time
        left_time = time % cycle
        if left_time >= self.move_time:
            return cycle_dist + self.move_time * self.speed
        else:
            return cycle_dist + left_time * self.speed

reindeers = {}

try:
    while True:
        string = input().split()
        name = string[0]
        speed = int(string[3])
        move_time = int(string[6])
        rest_time = int(string[13])
        reindeers[name] = Reindeer(name, speed, move_time, rest_time)
except EOFError:
    pass

time = 2503
distance = 0
for reindeer in reindeers:
    dist = reindeers[reindeer].find_distance(time)
    if distance < dist:
        distance = dist
print(distance)
