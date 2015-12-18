__author__ = 'oni'


class Segment:
    segment_history = []

    def __init__(self, segments):
        self.A = segments[0]
        self.B = segments[1]
        self.C = segments[2]
        self.D = segments[3]
        self.E = segments[4]
        self.F = segments[5]
        self.G = segments[6]
        self.p = segments[7]

        self.segment_history.append([self.A, self.B, self.C, self.D, self.E, self.F, self.G, self.p])

    def print_chars(self):

        out = self.build_output_string(self.segment_history, '')
        print out

    def build_output_string(self, history, output_string):

        if len(history) == 0:
            return output_string

        if history[0][:7] == [True, True, True, False, True, True, True]:
            output_string += 'A'
        if history[0][:7] == [True, False, True, True, False, True, True]:
            output_string += 'S'
        if history[0][:7] == [False, False, False, True, True, True, True]:
            output_string += 't'
        if history[0][:7] == [True, False, False, True, True, True, True]:
            output_string += 'E'
        if history[0][:7] == [False, False, False, False, True, False, True]:
            output_string += 'r'
        if history[0][:7] == [False, True, True, False, False, False, False]:
            output_string += '1'
        if history[0][:7] == [False, False, True, True, True, False, True]:
            output_string += 'o'
        if history[0][:7] == [False, False, True, False, True, False, True]:
            output_string += 'n'
        if history[0][:7] == [True, True, True, False, False, True, True]:
            output_string += '9'

        if history[0][7]:
            output_string += '.'

        return self.build_output_string(history[1:], output_string)

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

        return self.render(self.scale(result, 3))

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
            out = line.replace('0', ' ').replace('1', '\033[1;47m|\033[1;m').replace('2', '\033[1;47m-\033[1;m')
            print out
