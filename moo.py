#! /usr/bin/env python
import random
import socket
import sys
from sets import Set


# def initialize(data):
#   chosen = data['chosen']
#   in_port = data['in_port']
#   out_port = data['out_port']
#   past_guesses = Set([generate_number()])

def initialize(player):
  past_guesses = Set([generate_number()])


def router(data):
  #Receive message

  #


def server(data):
  chosen = data['chosen']
  guess = data['guess']
  guesses = data['guesses']
  '''
   Bulls and cows. A game pre-dating, and similar to, Mastermind.
  '''
  digits = '123456789'
  size = 4
  # chosen = ''.join(random.sample(digits,size))
  #print chosen # Debug
  # print '''I have chosen a number from %s unique digits from 1 to 9 arranged in a random order.
  # You need to input a %i digit, unique digit number as a guess at what I have chosen''' % (size, size)
  # guesses = 0
  while True:
      guesses += 1
      while True:
          # get a good guess
          # guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
          if len(guess) == size and \
             all(char in digits for char in guess) \
             and len(set(guess)) == size:
              break
          print "Problem, try again. You need to enter %i unique digits from 1 to 9" % size
      if guess == chosen:
          print '\nCongratulations you guessed correctly in',guesses,'attempts'
          data['bulls_cows'] = "4B0C"
          data['guesses'] = guesses
          data['win_status']="WIN"
          return data
          # break
      bulls = cows = 0
      for i in range(size):
          if guess[i] == chosen[i]:
              bulls += 1
          elif guess[i] in chosen:
              cows += 1
      print '  %i Bulls\n  %i Cows' % (bulls, cows)
      data['guesses'] = guesses
      data['win_status'] = "LOSS"
      data['bulls_cows'] = bulls.to_s + "B" + cows.to_s + "C"
      return data



def generate_number:
  digits = '123456789'
  size = 4
  guess = ''.join(random.sample(digits,size))
  return guess


player = []
if (len(sys.argv) == 4):
  player['number'] = sys.argv[1]
  player['in_port'] = sys.argv[2]
  player['out_port'] = sys.argv[3]

initialize(player)