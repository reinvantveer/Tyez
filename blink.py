import time

from pyfirmata import Arduino

board = Arduino('COM4')
print('what')


# Adapted from https://pastebin.com/8gSTrHs9
def blink(second):  # função blink usada para piscar led
 # board --> porta digital --> pino 13 write -> 1 Ligado
  board.digital[13].write(1)
  time.sleep(second)
 # board --> porta digital --> pino 13 write -> 0 desligado
  board.digital[13].write(0)
  time.sleep(second)


for _ in range(10):
    blink(1)

print('Done!')
