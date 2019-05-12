import argparse
import time

from util.board import get_board
from pyfirmata import util

ANALOG_PORT = 0

parser = argparse.ArgumentParser(
    description='REST API and web interface to Arduino analog port read',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('-p', '--port', required=True, help='COM port to communicate with the Arduino')
args = parser.parse_args()


if __name__ == '__main__':
    board = get_board(args.port)
    print('Connected!')

    it = util.Iterator(board)
    it.start()
    board.analog[ANALOG_PORT].enable_reporting()

    # Get rid of the first None value by giving the board time to initialize:
    time.sleep(1)

    while True:
        analog_val = board.analog[ANALOG_PORT].read()
        print(analog_val)
        time.sleep(1)

    # print('Done!')
