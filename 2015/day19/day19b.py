# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.
# However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.
# Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine.
#
# How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?
#
# Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.
#
# Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

################################################
# Just to be clear, I didn't solve it myself. I got idea from someone else, and put it in practice.
# And I don't actually need all this class thing, it just left from part 1.
################################################
class Rule():

    def __init__(self, name):

        self.name = name
        self.replace = set()

    def add_rule(self, replacement):

        self.replace.add(replacement)

class Message():

    def __init__(self,string):

        self.string = string
        self.indexes = self.get_indexes()
        self.next = self.get_all_next()
        self.step = None

    def add_step(self,step):

        self.step = step

    def get_indexes(self):

        indexes = {}
        for rule in rules:
            index = 0
            indexes[rule] = []
            while True:
                next_index = self.string.find(rule,index)
                if next_index != -1:
                    indexes[rule].append(next_index)
                    index = next_index + 1
                else:
                    break
        return indexes

    def get_all_next(self):

        new_strings = set()
        for rule in rules:
            for replace in rules[rule].replace:
                for index in self.indexes[rule]:
                    string = self.string
                    rule_len = len(rule)
                    new_string = string[:index]+replace+string[index+rule_len:]
                    new_strings.add(new_string)
        return new_strings

rules = {}
try:
    while True:
        rule = input()
        if '=>' in rule:
            rule = rule.split()[::2]
            name = rule[0]
            replacement = rule[1]
            if name not in rules:
                rules[name] = Rule(name)
            rules[name].add_rule(replacement)
        else:
            mess = Message(rule)
except EOFError:
    pass

# no need to count every step, because of the way Rn-Y-Ar look.
# It resembles a function, so I change them into something more lookable.
string = mess.string
i = 0
while i < len(string):
    if i != len(string)-1:
        if string[i] + string[i+1] == 'Rn':
            string = string[:i]+'('+string[i+2:]
        if string[i] + string[i+1] == 'Ar':
            string = string[:i]+')'+string[i+2:]
        if string[i] == 'Y':
            string = string[:i]+','+string[i+1:]
    # and delete the rest small numbers
    if ord(string[i]) >= 97 and ord(string[i]) <= 122:
        string = string[:i]+string[i+1:]
        continue
    i += 1

# usually by 1 step we add just another letter, so I just need to count length - 1 of every consecutive string.
count = 0
while '(' in string:
    end = string.find(')')
    start = string.rfind('(',0,end)
    mes = string[start+1:end]
    if ',' in mes:
        mes = mes.split(',')
        for item in mes:
            count += len(item) - 1
    else:
        count += len(mes) - 1

    # and add 1 for each function.
    string = string[:start]+string[end+1:]
    count += 1
count += len(string)-1
print(count)
