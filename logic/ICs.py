__author__ = 'oni'


class Counter4bit:

    def __init__(self):
        self.state = 0b0000

    def count(self):
        if self.state == 0b1111:
            self.state = 0b0000
        else:
            self.state += 1

    def reset(self):
        self.state = 0b0000


class TTL:

    def __init__(self, type, inputs):

        self.type = type
        self.pins = []

        self.pins.append(inputs[0])
        self.pins.append(inputs[1])
        self.pins.append(self.logic_op(inputs[0], inputs[1]))

        self.pins.append(self.logic_op(inputs[2], inputs[3]))
        self.pins.append(inputs[2])
        self.pins.append(inputs[3])

        self.pins.append('dummy GND')
        self.pins.append('dummy Vcc')

        self.pins.append(inputs[4])
        self.pins.append(inputs[5])
        self.pins.append(self.logic_op(inputs[4], inputs[5]))

        self.pins.append(self.logic_op(inputs[6], inputs[7]))
        self.pins.append(inputs[6])
        self.pins.append(inputs[7])

    def print_pins(self):
        print self.pins

    def logic_op(self, opA, opB):
        if self.type == '4081':
            return opA & opB
        else:
            return opA | opB
