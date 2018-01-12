# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.
#
# What signal is ultimately provided to wire a?
#
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a).
#
# What new signal is ultimately provided to wire a?

####################
# I decided not to implement code twice and just changed b-value in the second input file.
####################

# Represents wire
class dot:

    def __init__(self,name):
        self.name = name
        self.value = None

    def impl(self,value):
        self.value = value

# Create different gates.
# First create them with exact values, or Null values if wired
# Then put values if they are known
# Finally find out value of exit wire
class input_gate:

    def __init__(self,input_list):
        self.state = True
        try:
            self.st_value = int(input_list[0])
            self.start = None
        except ValueError:
            self.start = dots[input_list[0]].name
        self.end = dots[input_list[1]].name

    def put_val(self):
        if self.start != None:
            value = dots[self.start].value
            if value != None:
                self.st_value = value
                self.start = None

    def impl(self):
        if self.start == None:
            dots[self.end].impl(self.st_value)
            self.state = False

class not_gate:

    def __init__(self,not_list):
        self.state = True
        try:
            self.st_value = int(not_list[0])
            self.start = None
        except ValueError:
            self.start = dots[not_list[0]].name
        self.end = dots[not_list[1]].name

    def put_val(self):
        if self.start != None:
            value = dots[self.start].value
            if value != None:
                self.st_value = value
                self.start = None

    def impl(self):
        if self.start == None:
            dots[self.end].impl(65535 - self.st_value)
            self.state = False

class and_gate:

    def __init__(self,and_list):
        self.state = True
        try:
            self.st1_value = int(and_list[0])
            self.start1 = None
        except ValueError:
            self.start1 = dots[and_list[0]].name
        try:
            self.st2_value = int(and_list[1])
            self.start2 = None
        except ValueError:
            self.start2 = dots[and_list[1]].name
        self.end = dots[and_list[2]].name

    def put_val(self):
        if self.start1 != None:
            value1 = dots[self.start1].value
            if value1 != None:
                self.st1_value = value1
                self.start1 = None
        if self.start2 != None:
            value2 = dots[self.start2].value
            if value2 != None:
                self.st2_value = value2
                self.start2 = None

    def impl(self):
        if self.start1 == None and self.start2 == None:
            dots[self.end].impl(self.st1_value & self.st2_value)
            self.state = False

class or_gate:

    def __init__(self,or_list):
        self.state = True
        try:
            self.st1_value = int(or_list[0])
            self.start1 = None
        except ValueError:
            self.start1 = dots[or_list[0]].name
        try:
            self.st2_value = int(or_list[1])
            self.start2 = None
        except ValueError:
            self.start2 = dots[or_list[1]].name
        self.end = dots[or_list[2]].name

    def put_val(self):
        if self.start1 != None:
            value1 = dots[self.start1].value
            if value1 != None:
                self.st1_value = value1
                self.start1 = None
        if self.start2 != None:
            value2 = dots[self.start2].value
            if value2 != None:
                self.st2_value = value2
                self.start2 = None

    def impl(self):
        if self.start1 == None and self.start2 == None:
            dots[self.end].impl(self.st1_value | self.st2_value)
            self.state = False

class lshift_gate:

    def __init__(self,lshift_list):
        self.state = True
        try:
            self.st_value = int(lshift_list[0])
            self.start = None
        except ValueError:
            self.start = dots[lshift_list[0]].name
        self.step = int(lshift_list[1])
        self.end = dots[lshift_list[2]].name

    def put_val(self):
        if self.start != None:
            value = dots[self.start].value
            if value != None:
                self.st_value = value
                self.start = None

    def impl(self):
        if self.start == None:
            dots[self.end].impl(self.st_value << self.step)
            self.state = False

class rshift_gate:

    def __init__(self,rshift_list):
        self.state = True
        try:
            self.st_value = int(rshift_list[0])
            self.start = None
        except ValueError:
            self.start = dots[rshift_list[0]].name
        self.step = int(rshift_list[1])
        self.end = dots[rshift_list[2]].name

    def put_val(self):
        if self.start != None:
            value = dots[self.start].value
            if value != None:
                self.st_value = value
                self.start = None

    def impl(self):
        if self.start == None:
            dots[self.end].impl(self.st_value >> self.step)
            self.state = False


#initials
dots = {}
gate_num = 0
gates = {}
# Create gates and dots
try:
    while True:
        string = input().split()
        if len(string)%2 == 0:
            eff_params = string[1::2]
        else:
            eff_params = string[::2]
        for i in range(len(eff_params)):
            try:
                eff_params[i]=int(eff_params[i])
            except ValueError:
                dots[eff_params[i]] = dot(eff_params[i])

        if string[0] == 'NOT':
            gates[gate_num] = not_gate(eff_params)
        elif string[1] == 'AND':
            gates[gate_num] = and_gate(eff_params)
        elif string[1] == 'OR':
            gates[gate_num] = or_gate(eff_params)
        elif string[1] == 'LSHIFT':
            gates[gate_num] = lshift_gate(eff_params)
        elif string[1] == 'RSHIFT':
            gates[gate_num] = rshift_gate(eff_params)
        else:
            gates[gate_num] = input_gate(eff_params)
        gate_num += 1
except EOFError:
    pass

# Main
while dots['a'].value == None:
    for gate in gates:
        if gates[gate].state == True:
            gates[gate].put_val()
            gates[gate].impl()

print(dots['a'].value)
