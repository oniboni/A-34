__author__ = 'oni'

from segment import Segment
from logic.logicNet import LogicNet


def main():

    test_input = "01 23 45 67 89 ab cd ef"

    logic = LogicNet(int('b', 16))
    for char in test_input.replace(' ', ''):
        logic.read_input(int(char, 16))
        segment = Segment(logic.follow_paths())
        print segment.print_segment()


if __name__ == '__main__':
    main()
