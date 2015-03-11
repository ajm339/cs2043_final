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
    # chosen = ''.join(random.sample(digits,size))
    #print chosen # Debug
    # print '''I have chosen a number from %s unique digits from 1 to 9 arranged in a random order.
    # You need to input a %i digit, unique digit number as a guess at what I have chosen''' % (size, size)
    # guesses = 0
    while True:
        self.guesses += 1
        while True:
            # get a good guess
            # guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
            if len(guess) == size and \
               all(char in digits for char in guess) \
               and len(set(guess)) == size:
                break
            print "Problem, try again. You need to enter %i unique digits from 1 to 9" % size
        if guess == self.chosen:
            print '\nCongratulations you guessed correctly in',self.guesses,'attempts'
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
      self.new()
    else:
      self.past_guesses.add(guess)
      return guess


print "Starting Script"
print '=================='
PORT = {}
if (len(sys.argv) == 4):
  player_number = sys.argv[1]
  PORT['in'] = int(sys.argv[2])
  PORT['out'] = int(sys.argv[3])


game = BullsAndCows(player_number)

print game.check_guess("1245")

# guess = Guess()


# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# still_playing = True
# HOST = ''

# message = "GUESS:" + guess.new()
# sock.sendto(message, (HOST, PORT['out']))

# while still_playing:
#   print "still_playing"
#   sock.bind((HOST, PORT['in']))  

#   print "socket"

#   while still_playing:
#     print "receiving"
#     data, addr = sock.recvfrom(1024)
#     print "received message:", data
#     if("GUESS" in data):
#       print "GUESS"
#       index = data.index(":") + 1
#       number = data[index:]
#       game.check_guess(number)
#     elif("WIN" in data):
#       print "WIN"
#       still_playing = False
#     else:
#       print data
#       message = "GUESS:" + str(guess.new())
#       sock.sendto(message, (HOST, PORT['out']))