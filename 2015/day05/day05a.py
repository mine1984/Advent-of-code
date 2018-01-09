# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only).
# It contains at least one letter that appears twice in a row.
# It does not contain the strings ab, cd, pq, or xy.
#
# How many strings are nice?

class input_string:

    def __init__(self,string):
        self.string = string

    def is_nice(self):
        length = len(self.string)
        vowels = 0
        twice = False
        for i in range(length-1):
            double = self.string[i:i+2]
            if double == 'ab' or double == 'cd' or double == 'pq' or double == 'xy':
                return False
            if self.string[i] == self.string[i+1]:
                twice = True
            if self.string[i] in 'aeiou':
                vowels += 1
        if self.string[-1] in 'aeiou':
            vowels += 1
        if twice == True and vowels >= 3:
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
