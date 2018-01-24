# Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.
# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.
#
# After exactly 2503 seconds, what distance has the winning reindeer traveled?
#
# Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.)
#
# After exactly 2503 seconds, how many points does the winning reindeer have?

class Reindeer():

    def __init__(self, name, speed, move_time, rest_time):

        self.name = name
        self.speed = speed
        self.move_time = move_time
        self.rest_time = rest_time
        self.distance = 0
        self.score = 0

    def move(self, time):

        cycle = self.move_time + self.rest_time
        left_time = time % cycle
        if left_time > 0 and left_time <= self.move_time:
            self.distance += self.speed

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
for second in range(1,time+1):
    lead = []
    for reindeer in reindeers:
        reindeers[reindeer].move(second)
        if distance == reindeers[reindeer].distance:
            lead.append(reindeer)
        elif distance < reindeers[reindeer].distance:
            distance = reindeers[reindeer].distance
            lead = [reindeer]
    for reindeer in lead:
        reindeers[reindeer].score += 1

score = 0
for reindeer in reindeers:
    sc = reindeers[reindeer].score
    if score < sc:
        score = sc
print(score)
