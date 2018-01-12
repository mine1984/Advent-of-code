# It is common in many programming languages to provide a way to escape special characters in strings.
# However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.
#
# Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?
#
# In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.
#
# Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal.

class line():

    def __init__(self,string):

        self.length = len(string)

        self.len_mem_string = self.memory_string(string)
        self.diff1 = self.length - self.len_mem_string

        self.len_new_string = self.new_string(string)
        self.diff2 = self.len_new_string - self.length

    def memory_string(self,string):
        string = string[1:-1]
        while string.find('\\') != -1:
            slash = string.find('\\')
            if string[slash + 1] == '\\' or string[slash + 1] == '"':
                string = string[:slash]+'s'+string[slash+2:]
            else:
                string = string[:slash]+'x'+string[slash+4:]
        return len(string)

    def new_string(self,string):
        index = 0
        while index < len(string):
            if string[index] == '\\':
                string = string[:index+1]+'\\'+string[index+1:]
                index += 2
            elif string[index] == '"':
                string = string[:index+1]+'"'+string[index+1:]
                index += 2
            else:
                index += 1
        string = '"' + string + '"'
        return len(string)

count = 0
strings = {}
result1 = 0
result2 = 0
try:
    while True:
        string = input()
        strings[count] = line(string)
        result1 += strings[count].diff1
        result2 += strings[count].diff2
        count += 1
except EOFError:
    pass

print(result1,result2)
