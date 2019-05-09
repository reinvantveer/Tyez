import time
import argparse


from pyfirmata import Arduino
from serial import SerialException

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

print('Done!')
