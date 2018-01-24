# You have 500 Aunts named "Sue".
# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:
#
# children, by human DNA age analysis.
# cats. It doesn't differentiate individual breeds.
# Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
# goldfish. No other kinds of fish.
# trees, all in one group.
# cars, presumably by exhaust or gasoline or something.
# perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
# In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:
#
# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1
# You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.
#
# What is the number of the Sue that got you the gift?
#
# In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many.
#
# What is the number of the real Aunt Sue?

class Aunt():

    def __init__(self, string):

        self.name = string[1][:-1]
        self.clues = {}
        self.clues[string[2][:-1]] = int(string[3][:-1])
        self.clues[string[4][:-1]] = int(string[5][:-1])
        self.clues[string[6][:-1]] = int(string[7])
        self.is_sender = self.find_out()

    def find_out(self):
        for clue in self.clues:
            if clue == 'cats' or clue == 'trees':
                if self.clues[clue] <= gift[clue]:
                    return False
            elif clue == 'pomeranians' or clue == 'goldfish':
                if self.clues[clue] >= gift[clue]:
                    return False
            elif self.clues[clue] != gift[clue]:
                return False
        return True


gift = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

aunts = {}
try:
    while True:
        string = input().split()
        name = string[1][:-1]
        aunts[name] = Aunt(string)
except EOFError:
    pass

for aunt in aunts:
    if aunts[aunt].is_sender:
        print(aunt)
