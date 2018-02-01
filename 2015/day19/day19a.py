# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.
# However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.
# Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine.
#
# How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

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

print(len(mess.next))
