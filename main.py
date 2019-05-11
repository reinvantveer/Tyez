import argparse

from pyfirmata import Arduino
from serial import SerialException

from serial_scan.scan import get_com_ports
from util.yes_no import query_yes_no

parser = argparse.ArgumentParser(
  description='REST API and web interface to Arduino analog port read',
  formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument('-p', '--port', required=True, help='COM port to communicate with the Arduino')
args = parser.parse_args()

try:
  board = Arduino(args.port)
except SerialException as e:
  print('Unable to connect Arduino on port {}'.format(args.port))
  com_ports = get_com_ports()
  if len(com_ports) == 0:
    print('No COM ports in use detected. Is the Arduino connected?')
  elif len(com_ports) == 1:
    question = 'Found COM port ' + com_ports[0] + ', retry using this port?'
    answer = query_yes_no(question)
    if answer:
      board = Arduino(com_ports[0])
  else:
    print('I do have COM ports', ', '.join(com_ports), 'you may want to try one of these.')

print('Done!')
