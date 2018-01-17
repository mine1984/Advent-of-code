# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence.
# Starting with the digits in your puzzle input, apply this process 40 times.
#
# What is the length of the result?
#
# Now, starting again with the digits in your puzzle input, apply this process 50 times.
#
# What is the length of the new result?

class lns():

    def __init__(self, name, init_value):

        self.name = name
        self.init_value = init_value
        self.value = self.create_value()

    def create_value(self):
        string = self.init_value
        value = ''
        for i in range(len(string)):
            if i == 0:
                ex = string[i]
                ex_index = i
                continue
            if i != len(string)-1:
                if string[i] == ex:
                    continue
                else:
                    value += str(i - ex_index) + ex
                    ex = string[i]
                    ex_index = i
            else:
                if string[i] == ex:
                    value += str(i - ex_index + 1) + ex
                else:
                    value += str(i - ex_index) + ex
                    value += '1' + string[i]

        return value

look = {-1:input()}

for i in range(50):
    if i == 0:
        look[i] = lns(i,look[-1])
    else:
        look[i] = lns(i,look[i-1].value)

print(len(look[39].value))
print(len(look[49].value))
