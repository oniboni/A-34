__author__ = 'oni'

class LogicNet:
    DEBUG = False

    def __init__(self, binaryInput):
        self.readInput(binaryInput)

    def readInput(self, binaryInput):
        #U1 binary count
        self.Q0 = binaryInput & 0b0001              == 1 # force binary type
        self.Q1 = (binaryInput & 0b0010) >> 1       == 1
        self.Q2 = (binaryInput & 0b0100) >> 2       == 1
        self.Q3 = (binaryInput & 0b1000) >> 3       == 1

        if self.DEBUG:
            print self.Q0, self.Q1, self.Q2, self.Q3

    def followPaths(self):
        #U2
        # U2_0 = self.Q0
        U2_1 = not self.Q0
        # U2_2 = self.Q1
        U2_3 = not self.Q1
        # U2_4 = self.Q2
        U2_5 = not self.Q2
        U2_12 = self.Q3
        U2_13 = not self.Q3

        U3 = IC( 'and', [
            U2_5, U2_3,                 #0,1
            U2_12, self.Q1,             #4,5
            U2_1, U2_13,                #8,9
            self.Q0, U2_12 & self.Q1    #12,13
        ])

        U4 = IC( 'and', [
            U2_13, self.Q1,             #0,1
            U2_13, U3.pins[0],          #4,5
            U3.pins[0], U2_12,          #8,9
            U3.pins[1], U3.pins[4]      #12,13
        ])

        U5 = IC( 'and', [
            U2_13, self.Q2,             #0,1
            U4.pins[12], U3.pins[12],   #4,5
            U4.pins[12] & U3.pins[12], self.Q2 & U2_12,  #8,9 =U8 8&9
            U4.pins[10], U3.pins[5]      #12,13
        ])

        U6 = IC( 'and', [
            U4.pins[11], U3.pins[8],    #0,1
            U4.pins[3], U3.pins[12],    #4,5
            U3.pins[12], U4.pins[10],   #8,9
            U3.pins[8], U4.pins[10]     #12,13
        ])

        U7 = IC( 'and', [
            U4.pins[10], U5.pins[13],   #0,1
            U5.pins[2], U5.pins[8],     #4,5
            U6.pins[1], U4.pins[12] & U4.pins[3],  #8,9
            U4.pins[12], U4.pins[3]     #12,13
        ])

        U8 = IC( 'and', [
            U5.pins[2], U7.pins[1],     #0,1
            U4.pins[2], U5.pins[12],    #4,5
            U5.pins[1], U4.pins[13],    #8,9
            U5.pins[11], U5.pins[1]     #12,13
        ])

        U9 = IC( 'or', [
            U3.pins[2], U6.pins[2],     #0,1
            U7.pins[2], U7.pins[3],     #4,5
            U8.pins[2], U3.pins[11],    #8,9
            U6.pins[10], U3.pins[11]    #12,13
        ])

        U10 = IC( 'or', [
            U3.pins[10], U8.pins[4],     #0,1
            U7.pins[2], U7.pins[13],     #4,5
            U6.pins[12], U6.pins[0],     #8,9
            U7.pins[13], U6.pins[11]     #12,13
        ])

        U11 = IC( 'or', [
            U10.pins[3], U10.pins[10],    #0,1
            U9.pins[2], U10.pins[11],     #4,5
            U5.pins[10], U8.pins[11] | U10.pins[2],    #8,9
            U8.pins[11], U10.pins[2]      #12,13
        ])

        U12 = IC( 'or', [
            U9.pins[1], U6.pins[3],       #0,1
            U9.pins[1] | U6.pins[3], U8.pins[3],     #4,5
            U9.pins[10], U9.pins[3] | U9.pins[2],    #8,9
            U9.pins[3], U9.pins[2]        #12,13
        ])

        U13 = IC( 'or', [
            U9.pins[11], U12.pins[12],       #0,1
            U9.pins[11] | U12.pins[12], U8.pins[3],     #4,5
            U10.pins[13], U12.pins[1] | U12.pins[13],    #8,9
            U12.pins[1], U12.pins[13]        #12,13
        ])

        if self.DEBUG:
            print U2_1, U2_5, U2_12, U2_13
            U3.printPins()
            U4.printPins()
            U5.printPins()
            U6.printPins()



        G = U11.pins[2]
        F = U11.pins[3]
        A = U13.pins[10]
        B = U13.pins[3]
        E = U11.pins[10]
        D = U12.pins[3]
        C = U12.pins[10]
        p = U2_1

        return [ A, B, C, D, E, F, G, p]

class IC:
    def __init__(self, type, inputs):

        self.type = type
        self.pins = []

        self.pins.append(inputs[0])
        self.pins.append(inputs[1])
        self.pins.append(self.logicOp(inputs[0], inputs[1]))

        self.pins.append(self.logicOp(inputs[2], inputs[3]))
        self.pins.append(inputs[2])
        self.pins.append(inputs[3])

        self.pins.append('dummy GND')
        self.pins.append('dummy Vcc')

        self.pins.append(inputs[4])
        self.pins.append(inputs[5])
        self.pins.append(self.logicOp(inputs[4], inputs[5]))

        self.pins.append(self.logicOp(inputs[6], inputs[7]))
        self.pins.append(inputs[6])
        self.pins.append(inputs[7])

    def printPins(self):
        print self.pins

    def logicOp(self, opA, opB):
        if self.type == 'and':
            return opA & opB
        else:
            return opA | opB