# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once.
#
# What is the shortest distance he can travel to achieve this?
#
# What is the distance of the longest route?

class town():

    def __init__(self, name):

        self.name = name
        self.roads = {}
        self.paths = {}
        self.short = None
        self.long = None

    def add_road(self, name, length):

        self.roads[name] = length

    #DFS
    def init_path_find(self):
        visited = {key:0 for key in towns}
        path = []
        self.find_paths(self.name, visited, path)

    def find_paths(self, town, visited, path):
        visited[town] = 1
        path.append(town)
        if sum(visited.values()) == len(towns):
            self.paths[tuple(path)] = self.find_length(path)
        else:
            for next_town in towns:
                if visited[next_town] == 0:
                    self.find_paths(next_town, visited, path)
        path.pop()
        visited[town] = 0

    def find_length(self, path):
        result = 0
        for index in range(len(path)-1):
            start = path[index]
            end = path[index+1]
            result += towns[start].roads[end]
        return result

    def find_short(self):
        return min(self.paths.items(), key = lambda x: x[1])[0]

    def find_long(self):
        return max(self.paths.items(), key = lambda x: x[1])[0]


towns = {}

try:
    while True:
        string = input().split()[::2]
        if string[0] not in towns:
            towns[string[0]] = town(string[0])
        if string[1] not in towns:
            towns[string[1]] = town(string[1])
        towns[string[0]].add_road(string[1],int(string[2]))
        towns[string[1]].add_road(string[0],int(string[2]))
except EOFError:
    pass

short_d = 1000
long_d = 0
for town in towns:
    towns[town].init_path_find()
    towns[town].short = towns[town].find_short()
    towns[town].long = towns[town].find_long()
    if short_d > towns[town].paths[towns[town].short]:
        short_d = towns[town].paths[towns[town].short]
    if long_d < towns[town].paths[towns[town].long]:
        long_d = towns[town].paths[towns[town].long]
print(short_d)
print(long_d)
