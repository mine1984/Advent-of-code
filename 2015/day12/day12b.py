# They have a JSON document which contains a variety of things: arrays, objects, numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.
# You will not encounter any strings containing numbers.
#
# What is the sum of all numbers in the document?
#
# Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects, not arrays.

def to_delete(string,red_index):
    obj_start = string.rfind('{', 0, red_index)
    obj_end = string.find('}', red_index+1)
    count = 0

    #find first open bracket, so 'red' was it's key's value
    while True:
        for i in range(obj_start, red_index+1):
            if string[i] == '{':
                count += 1
            if string[i] == '}':
                count += -1
        if count == 1:
            break
        else:
            obj_start = string.rfind('{', 0, obj_start)
            count = 0

    #find last close bracket, so 'red' was it's key's value
    count = 0
    while True:
        for i in range(red_index, obj_end+1):
            if string[i] == '{':
                count += 1
            if string[i] == '}':
                count += -1
        if count == -1:
            break
        else:
            obj_end = string.find('}', obj_end+1)
            count = 0

    return obj_start, obj_end

string = input()

while True:
    red_index = string.find('red')
    if red_index == -1:
        break
    # check if it's not object
    if string[red_index - 2] != ':':
        string = string[:red_index] + string[red_index+1:]
        continue
    else:
        obj_start, obj_end = to_delete(string,red_index)
        string = string[:obj_start] + string[obj_end+1:]

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
