__author__ = 'oni'

from segment import Segment
from logic.logicNet import LogicNet


def main():

    # cheap hex counter simulation :)
    test_input = "01 23 45 67 89 ab cd ef"   # "01 b0 c4 81 a6 c5 81 a0 5f 01 b7 5f"

    logic = LogicNet(int('b', 16))
    for char in test_input.replace(' ', ''):
        logic.read_input(int(char, 16))
        segment = Segment(logic.follow_paths())
        # print segment.print_segment()

    segment.print_chars()


if __name__ == '__main__':
    main()
