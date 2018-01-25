# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.
#
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
#
# Find the minimum number of containers that can exactly fit all 150 liters of eggnog.
#
# How many different ways can you fill that number of containers and still hold exactly 150 litres?

################################################################
# It has awful time complexity. I got no idea how to optimise. #
################################################################


class Container():

    def __init__(self, name, amount):

        self.name = name
        self.amount = int(amount)
        self.combinations = []

    #DFS
    def init_combination_find(self):
        visited = {key:0 for key in containers}
        combination = []
        self.find_combinations(self.name, visited, combination)

    def find_combinations(self, container, visited, combination):
        visited[container] = 1
        combination.append(container)
        total = sum(containers[item].amount for item in combination)
        if total == 150:
            if set(combination) not in self.combinations:
                self.combinations.append(set(combination))
        elif total < 150:
            for next_container in containers:
                if visited[next_container] == 0 and next_container not in used:
                    self.find_combinations(next_container,visited,combination)
        combination.pop()
        visited[container] = 0

# create containers
containers = {}
count = 0
try:
    while True:
        amount = input()
        containers[count] = Container(count, amount)
        count += 1
except EOFError:
    pass

# implement finding the combination of containers. Bonus one way of optimisation.
used = []
for container in containers:
    containers[container].init_combination_find()
    used.append(container)

# collect all combinations, and find smallest.
combo = []
min_len = 20
for container in containers:
    for combination in containers[container].combinations:
        if combination not in combo:
            combo.append(combination)
            if len(combination) < min_len:
                min_len = len(combination)
print(len(combo))

# count smallest combinations.
count = 0
for item in combo:
    if len(item) == min_len:
        count += 1
print(count)
