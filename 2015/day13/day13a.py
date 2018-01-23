# In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.
# You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.
#
# What is the total change in happiness for the optimal seating arrangement of the actual guest list?

class person():

    def __init__(self, name):

        self.name = name
        self.relations = {}
        self.sits = {}
        self.big = None

    def add_relation(self, name, value):

        self.relations[name] = value

    #DFS
    def init_sit_find(self):
        visited = {key:0 for key in persons}
        sit = []
        self.find_sits(self.name, visited, sit)

    def find_sits(self, person, visited, sit):
        visited[person] = 1
        sit.append(person)
        if sum(visited.values()) == len(persons):
            self.sits[tuple(sit)] = self.find_relation(sit)
        else:
            for next_person in persons:
                if visited[next_person] == 0:
                    self.find_sits(next_person, visited, sit)
        sit.pop()
        visited[person] = 0

    def find_relation(self, sit):
        result = 0
        for index in range(len(sit)):
            person = sit[index]
            if index == 0:
                left = sit[-1]
            else:
                left = sit[index-1]
            if index == len(sit)-1:
                right = sit[0]
            else:
                right = sit[index+1]
            result += persons[person].relations[left] + persons[person].relations[right]
        return result

    def find_short(self):
        return min(self.paths.items(), key = lambda x: x[1])[0]

    def find_big(self):
        return max(self.sits.items(), key = lambda x: x[1])[0]


persons = {}

try:
    while True:
        string = input().split()
        first = string[0]
        second = string[-1][:-1]
        sign = string[2]
        if sign == 'gain':
            value = int(string[3])
        else:
            value = -int(string[3])
        if first not in persons:
            persons[first] = person(first)
        persons[first].add_relation(second, value)
except EOFError:
    pass

big_relation = 0
for person in persons:
    persons[person].init_sit_find()
    persons[person].big = persons[person].find_big()
    if big_relation < persons[person].sits[persons[person].big]:
        big_relation = persons[person].sits[persons[person].big]
print(big_relation)
