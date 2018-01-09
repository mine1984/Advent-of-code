# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive;
#
# After following the instructions, how many lights are lit?

class bulb:

    def __init__(self,name,i,j):
        self.name = name
        self.x = i
        self.y = j
        self.state = 0

    def impl(self,inst):
        if inst == 'on':
            self.state = 1
        if inst == 'off':
            self.state = 0
        if inst == 'toggle':
            self.state = 1 - self.state

# Create bulbs
bulbs = {}
for j in range(1000):
    for i in range(1000):
        name = str(j*1000+i)
        bulbs[name] = bulb(name,i,j)

try:
    while True:
        # Read instruction
        string = input().split()
        if string[0] == 'turn':
            string.pop(0)
        inst = string[0]
        coord1 = string[1].split(',')
        coord2 = string[3].split(',')
        x1 = int(coord1[0])
        y1 = int(coord1[1])
        x2 = int(coord2[0])
        y2 = int(coord2[1])

        # Implement instruction
        for j in range(y1,y2+1):
            for i in range(x1,x2+1):
                name = str(j*1000+i)
                #print(inst, bulbs[name].name)
                bulbs[name].impl(inst)
except EOFError:
    pass

# Find number of lit bulbs
result = 0
for j in range(1000):
    for i in range(1000):
        name = str(j*1000+i)
        if bulbs[name].state == 1:
            result += 1
print(result)
