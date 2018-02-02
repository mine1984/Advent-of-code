# To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.
# Each Elf is assigned a number, too, and delivers presents to houses based on that numberself.
# There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.
#
# What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?
#
# The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.
#
# What is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

#############################################
# This one is much quicker, thanks to restriction of 50 elfs per house.
# But still has bad time complexity. I got no idea how to solve it.
#############################################

from math import sqrt

class House():

    def __init__(self,num):

        self.num = num
        self.presents = None

    def sum_presents(self):

        value = 0
        edge = (self.num-1) //50
        if edge <= int(sqrt(self.num)):
            for i in range(1,1+edge):
                if self.num % i == 0:
                    value += 11 * houses[int(self.num/i)].num
            for i in range(1+edge,int(sqrt(self.num))+1):
                if self.num % i == 0:
                    if self.num != i**2:
                        value += 11 * (houses[i].num + houses[int(self.num/i)].num)
                    else:
                        value += 11 * houses[i].num
        else:
            for i in range(1,int(sqrt(self.num))+1):
                if self.num % i == 0:
                    if int(self.num/i) > edge:
                        value += 11 * houses[int(self.num/i)].num
        return value

value = int(input())
houses = {}
num = 1
while True:
    houses[num] = House(num)
    houses[num].presents = houses[num].sum_presents()
    if houses[num].presents >= value:
        print(num)
        break
    num += 1
