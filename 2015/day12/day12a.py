# They have a JSON document which contains a variety of things: arrays, objects, numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.
# You will not encounter any strings containing numbers.
#
# What is the sum of all numbers in the document?

string = input()
i = 0
result = 0
while i < len(string):
    # check if number started
    try:
        int(string[i])
        j = 1
        while True:
            try:
                int(string[i+j])
                j += 1
            # check if number ended
            except ValueError:
                num = string[i:i+j]
                # check if it's negative
                if string[i-1] == '-':
                    result += -int(num)
                else:
                    result += int(num)
                break
        i += j
    except ValueError:
        i += 1
print(result)
