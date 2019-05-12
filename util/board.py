import sys

from pyfirmata import Arduino
from serial import SerialException

from serial_scan.scan import get_com_ports
from util.yes_no import query_yes_no


def get_board(port):
    try:
        board = Arduino(port)
        return board
    except SerialException as e:
        print('Unable to connect Arduino on port {}'.format(port))
        com_ports = get_com_ports()
        if len(com_ports) == 0:
            print('No COM ports in use detected. Is the Arduino connected?')
            sys.exit(1)
        elif len(com_ports) == 1:
            question = 'Found COM port ' + com_ports[0] + ', retry using this port?'
            answer = query_yes_no(question)
            if answer:
                board = Arduino(com_ports[0])
                return board
            else:
                print('Exiting')
                sys.exit(1)
        else:
            print('I do have COM ports', ', '.join(com_ports), 'you may want to try one of these.')

