# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:
#
# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
#
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.
#
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

# parameters of four ingredients
class Ingredient():

    def __init__(self, string):

        self.name = string[0][:-1]
        self.capacity = int(string[1][:-1])
        self.durability = int(string[2][:-1])
        self.flavor = int(string[3][:-1])
        self.texture = int(string[4][:-1])
        self.calories = int(string[5])

# parameters of each recipy
class Recipe():

    def __init__(self,name,sp,pe,fr,su):

        self.name = name
        self.sp = sp
        self.pe = pe
        self.fr = fr
        self.su = su
        self.capacity = self.find_capacity()
        self.durability = self.find_durability()
        self.flavor = self.find_flavor()
        self.texture = self.find_texture()
        self.total = self.find_total()
        self.calories = self.find_calories()

    def find_capacity(self):

        value = ingredients['Sprinkles'].capacity * self.sp + ingredients['PeanutButter'].capacity * self.pe + ingredients['Frosting'].capacity * self.fr + ingredients['Sugar'].capacity * self.su
        if value < 0:
            value = 0
        return value

    def find_durability(self):

        value = ingredients['Sprinkles'].durability * self.sp + ingredients['PeanutButter'].durability * self.pe + ingredients['Frosting'].durability * self.fr + ingredients['Sugar'].durability * self.su
        if value < 0:
            value = 0
        return value

    def find_flavor(self):

        value = ingredients['Sprinkles'].flavor * self.sp + ingredients['PeanutButter'].flavor * self.pe + ingredients['Frosting'].flavor * self.fr + ingredients['Sugar'].flavor * self.su
        if value < 0:
            value = 0
        return value

    def find_texture(self):

        value = ingredients['Sprinkles'].texture * self.sp + ingredients['PeanutButter'].texture * self.pe + ingredients['Frosting'].texture * self.fr + ingredients['Sugar'].texture * self.su
        if value < 0:
            value = 0
        return value

    def find_total(self):
        return self.capacity * self.durability * self.flavor * self.texture

    def find_calories(self):

        value = ingredients['Sprinkles'].calories * self.sp + ingredients['PeanutButter'].calories * self.pe + ingredients['Frosting'].calories * self.fr + ingredients['Sugar'].calories * self.su
        return value

# create ingredients
ingredients = {}
try:
    while True:
        string = input().split()[::2]
        name = string[0][:-1]
        ingredients[name] = Ingredient(string)
except EOFError:
    pass

# create recipies. The idea is to use stars and bars from combinatorics.
recipies = {}
for i in range(101):
    for j in range(i+1,102):
        for k in range(j+1,103):
            sp = i
            pe = j-i-1
            fr = k-j-1
            su = 102-k
            name = str(sp) + '_' + str(pe) + '_' + str(fr) + '_' + str(su)
            recipies[name] = Recipe(name,sp,pe,fr,su)

max_total = 0
max_recipy = None
for recipy in recipies:
    if max_total < recipies[recipy].total:
        max_total = recipies[recipy].total
        max_recipy = recipy
print(max_recipy, max_total)

max_total = 0
max_recipy = None
for recipy in recipies:
    if recipies[recipy].calories == 500:
        if max_total < recipies[recipy].total:
            max_total = recipies[recipy].total
            max_recipy = recipy
print(max_recipy, max_total)
