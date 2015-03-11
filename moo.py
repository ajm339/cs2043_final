#! /usr/bin/env python
import random
import socket
import SocketServer
import sys
from sets import Set


class BullsAndCows:

  def __init__(self, chosen):
    self.chosen = chosen
    self.guesses = 0

  def check_guess(self, guess):
    digits = '123456789'
    size = 4
    while True:
        self.guesses += 1
        while True:
            if len(guess) == size and \
               all(char in digits for char in guess) \
               and len(set(guess)) == size:
                break
            print "Problem, try again. You need to enter %i unique digits from 1 to 9" % size
            return
        if guess == self.chosen:
            response="WIN"
            return response
            # break
        bulls = cows = 0
        for i in range(size):
            if guess[i] == self.chosen[i]:
                bulls += 1
            elif guess[i] in self.chosen:
                cows += 1
        print '  %i Bulls\n  %i Cows' % (bulls, cows)
        response = str(bulls) + "B" + str(cows) + "C"
        return response

class Guess:

  def __init__(self):
    self.past_guesses = Set([])

  def new(self):
    digits = '123456789'
    size = 4
    guess = ''.join(random.sample(digits,size))
    if guess in self.past_guesses:
      return self.new()
    else:
      self.past_guesses.add(guess)
      return guess


print "Starting Game"
print '===================================='
print ''
print ''

if (len(sys.argv) == 4):
  player_number = sys.argv[1]
  PORT_IN = int(sys.argv[2])
  PORT_OUT = int(sys.argv[3])

game = BullsAndCows(player_number)
guess = Guess()

still_playing = True
HOST = ''

message = "GUESS:" + guess.new()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT_IN))  

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(message, (HOST, PORT_OUT))

while (still_playing):

  data, addr = sock.recvfrom(1024)
  print "Received Message:" + data

  if("GUESS" in data):
    index = data.index(":") + 1
    number = data[index:]
    response = game.check_guess(number)
    if("WIN" in response):
      s.sendto(response, (HOST, PORT_OUT))
      print "YOU LOST. Goodbye."
      break
    else:
      print "Your opponent received x Bulls and y Cows: " + response
      s.sendto(response, (HOST, PORT_OUT))
  elif("WIN" in data):
    print "YOU WIN"
    still_playing = False
    break
  else:
    print "Your guess recevied x Bulls and y Cows: " + data
    message = "GUESS:" + str(guess.new())
    print "  Next Guess: " + message
    s.sendto(message, (HOST, PORT_OUT))

