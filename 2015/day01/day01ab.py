# He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
#
# To what floor do the instructions take Santa?
#
# Find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
#
# What is the position of the character that causes Santa to first enter the basement?

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
