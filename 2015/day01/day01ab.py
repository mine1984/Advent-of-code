result = 0
step = 0
s=input()
printed = False
for letter in s:
    step += 1
    if letter == '(':
        result += 1
    else:
        result += -1
    if result == -1:
        if not printed:
            print(step)
            printed = True
print(result)
