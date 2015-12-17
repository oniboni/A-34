__author__ = 'oni'


class Segment:

    def __init__(self, segments):
        self.A = segments[0]
        self.B = segments[1]
        self.C = segments[2]
        self.D = segments[3]
        self.E = segments[4]
        self.F = segments[5]
        self.G = segments[6]
        self.p = segments[7]

    def print_segment(self):

        result = ['000', '000', '000', '000', '000']

        if self.A:
            result[0] = '020'
        if self.B:
            result[1] = '001'
        if self.C:
            result[3] = '001'
        if self.D:
            result[4] = '020'
        if self.E:
            if result[3] == '001':
                result[3] = '101'
            else:
                result[3] = '100'
        if self.F:
            if result[1] == '001':
                result[1] = '101'
            else:
                result[1] = '100'
        if self.G:
            result[2] = '020'
        # if self.p:
        #     result[4][2] = '.'

        self.render(self.scale(result, 3))

    # copy&paste from https://stackoverflow.com/questions/18427782/seven-segment-display-with-width
    @staticmethod
    def scale(code, factor):
        if factor == 1:
            return code

        result = ["{}{}{}".format(line[0], line[1:-1]*factor, line[-1])  # widen
                  for line in code]

        for i in range(len(result)-2, 0, -2):
            result[i:i+1] = result[i:i+1]*factor       # stretch vertically

        return result

    # @staticmethod
    def render(self, code):

        if self.p:
            code[len(code)-1] += '.'

        for line in code:
            print(line.replace('0', ' ').replace('1', '|').replace('2', '-'))
