# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.
# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:
#
# Passwords must include one increasing straight of at least three letters.
# Passwords may not contain the letters i, o, or l.
# Passwords must contain at least two different, non-overlapping pairs of letters.
#
# Given Santa's current password (your puzzle input), what should his next password be?
#
# Santa's password expired again. What's the next one?

# inc one letter, and check if we need to increment next
def inc_letter(letter, adder):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if adder == 1:
        if letter == 'z':
            return 'a', 1
        else:
            new_letter = alpha[alpha.index(letter)+1]
            return new_letter, 0
    else:
        return letter, 0

# inc whole word
def inc_word(word):
    new_word = ''
    adder = 1
    for letter in reversed(word):
        new_letter, adder = inc_letter(letter, adder)
        new_word = new_letter + new_word
    return new_word

def check_rule1(word):
    for i in range(len(word)-2):
        l1 = word[i]
        l2 = word[i+1]
        l3 = word[i+2]
        if ord(l2)-ord(l1)==1 and ord(l3)-ord(l2)==1:
            return True
    return False

def check_rule2(word):
    for letter in word:
        if letter == 'i' or letter == 'o' or letter == 'l':
            return False
    return True

# Idea is to get all dubles without overlaping.
# And thencheck their difference using set.
def check_rule3(word):
    dubles = []
    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            dubles.append(word[i])
            i += 2
        else:
            i += 1
    dubles = set(dubles)
    if len(dubles) < 2:
        return False
    else:
        return True

# main
word = input()
while True:
    word = inc_word(word)
    if check_rule1(word) and check_rule2(word) and check_rule3(word):
        break
print(word)
while True:
    word = inc_word(word)
    if check_rule1(word) and check_rule2(word) and check_rule3(word):
        break
print(word)
