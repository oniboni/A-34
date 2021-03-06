__author__ = 'oni'

from ICs import TTL


class LogicNet:
    DEBUG = False

    def __init__(self, binary_input):
        self.read_input(binary_input)

    def read_input(self, binary_input):
        # U1 binary count
        self.Q0 = binary_input & 0b0001 == 1  # force binary type
        self.Q1 = (binary_input & 0b0010) >> 1 == 1
        self.Q2 = (binary_input & 0b0100) >> 2 == 1
        self.Q3 = (binary_input & 0b1000) >> 3 == 1

        if self.DEBUG:
            print self.Q0, self.Q1, self.Q2, self.Q3

    def follow_paths(self):
        # U2
        # U2_0 = self.Q0
        U2_1 = not self.Q0
        # U2_2 = self.Q1
        U2_3 = not self.Q1
        # U2_4 = self.Q2
        U2_5 = not self.Q2
        U2_12 = self.Q3
        U2_13 = not self.Q3

        U3 = TTL('4081', [          # out: 2,3,10,11
            U2_5, U2_3,                 # 0,1
            U2_12, self.Q1,             # 4,5
            U2_1, U2_13,                # 8,9
            self.Q0, U2_12 & self.Q1    # 12,13
        ])

        U4 = TTL('4081', [
            U2_13, self.Q1,             # 0,1
            U2_13, U2_5,                # 4,5
            U2_5, U2_12,                # 8,9
            U2_3, U2_12                 # 12,13
        ])

        U5 = TTL('4081', [
            U2_13, self.Q2,             # 0,1
            U4.pins[12], U3.pins[12],   # 4,5
            U4.pins[12] & U3.pins[12], self.Q2 & U2_12,  # 8,9 =U8 8&9
            U3.pins[8], U3.pins[5]      # 12,13
        ])

        U6 = TTL('4081', [
            U4.pins[11], U3.pins[8],    # 0,1
            U4.pins[3], U3.pins[12],    # 4,5
            U3.pins[12], U4.pins[10],   # 8,9
            U3.pins[8], U4.pins[10]     # 12,13
        ])

        U7 = TTL('4081', [
            U4.pins[10], U5.pins[13],   # 0,1
            U5.pins[2], U5.pins[8],     # 4,5
            U6.pins[1], U4.pins[12] & U4.pins[3],  # 8,9
            U4.pins[12], U4.pins[3]     # 12,13
        ])

        U8 = TTL('4081', [
            U5.pins[2], U7.pins[1],     # 0,1
            U4.pins[2], U5.pins[12],    # 4,5
            U5.pins[1], U4.pins[13],    # 8,9
            U5.pins[11], U5.pins[1]     # 12,13
        ])

        U9 = TTL('4071', [
            U3.pins[2], U6.pins[2],     # 0,1
            U7.pins[2], U7.pins[3],     # 4,5
            U8.pins[2], U3.pins[11],    # 8,9
            U6.pins[10], U3.pins[11]    # 12,13
        ])

        U10 = TTL('4071', [
            U3.pins[10], U8.pins[4],     # 0,1
            U7.pins[13], U8.pins[4],     # 4,5
            U6.pins[1], U6.pins[0],      # 8,9
            U7.pins[13], U6.pins[11]     # 12,13
        ])

        U11 = TTL('4071', [
            U10.pins[3], U10.pins[10],    # 0,1
            U9.pins[2], U10.pins[11],     # 4,5
            U5.pins[10], U8.pins[11] | U10.pins[2],    # 8,9
            U8.pins[11], U10.pins[2]      # 12,13
        ])

        U12 = TTL('4071', [
            U9.pins[1], U6.pins[3],       # 0,1
            U9.pins[1] | U6.pins[3], U8.pins[3],     # 4,5
            U9.pins[10], U9.pins[3] | U9.pins[2],    # 8,9
            U9.pins[3], U9.pins[2]        # 12,13
        ])

        U13 = TTL('4071', [
            U9.pins[11], U12.pins[12],       # 0,1
            U9.pins[11] | U12.pins[12], U7.pins[10],     # 4,5
            U10.pins[13], U12.pins[1] | U12.pins[13],    # 8,9
            U12.pins[1], U12.pins[13]        # 12,13
        ])

        if self.DEBUG:
            print U2_1, U2_5, U2_12, U2_13
            U3.print_pins()
            U4.print_pins()
            U5.print_pins()
            U6.print_pins()

        G = U11.pins[2]
        F = U11.pins[3]
        A = U13.pins[10]
        B = U13.pins[3]
        E = U11.pins[10]
        D = U12.pins[3]
        C = U12.pins[10]
        p = U8.pins[5]

        return [A, B, C, D, E, F, G, p]
