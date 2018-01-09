# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only).
# It contains at least one letter that appears twice in a row.
# It does not contain the strings ab, cd, pq, or xy.
#
# How many strings are nice?
#
# Now, a nice string is one with all of the following properties:
#
# It contains a pair of any two letters that appears at least twice in the string without overlapping.
# It contains at least one letter which repeats with exactly one letter between them.
#
# How many strings are nice under these new rules?

class input_string:

    def __init__(self,string):
        self.string = string

    def is_nice(self):
        length = len(self.string)
        pair = False
        between = False
        for i in range(length-2):
            double = self.string[i:i+2]
            index2 = string.find(double,i+2)
            if index2 != -1:
                pair = True
            if self.string[i] == self.string[i+2]:
                between = True
        if pair == True and between == True:
            return True
        else:
            return False


strings = []
s_id = 0
result = 0
try:
    while True:
        string = input()
        strings.append(input_string(string))
        if strings[s_id].is_nice():
            result += 1
        s_id += 1
except EOFError:
    pass
print(result)
