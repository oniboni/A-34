__author__ = 'oni'

from segment import Segment
from logic.logicNet import LogicNet

def main():
    input = "01 b0 c4 81 a6 c5 81 a0 5f 01 b7 5f"

    logic = LogicNet(int('b',16))
    for char in input.replace(' ', ''):
        logic.readInput(int(char,16))
        segment = Segment(logic.followPaths())
        print segment.printSegment()


if __name__ == '__main__':
    main()