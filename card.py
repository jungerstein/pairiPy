__author__ = 'candyfeline'

# M: 1 2 3 4 5 6 7 8 9
# P: 11 12 13 14 15 16 17 18 19
# S: 21 22 23 24 25 26 27 28 29
# JI: 31 32 33 34 35 36 37

primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23]
primeKokushi = primeList + [29, 31, 37, 41]
kokushiList = {
  1:  2,  9:  3,
  11: 5,  19: 7,
  21: 11, 29: 13,
  31: 17, 32: 19, 33: 23, 34: 29,
  35: 31, 36: 37, 37: 41
}

def handToCardgroup(hand):
  hand.sort()
  manzu = [card for card in hand if card < 10]
  pinzu = [card - 10 for card in hand if 10 <= card < 20]
  sozu = [card - 20 for card in hand if 20 <= card < 30]
  jihai = [card - 30 for card in hand if card > 30]
  return (manzu, pinzu, sozu, jihai)

def cardHash(cardSuit):
  primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
  hash = 1
  for card in cardSuit:
    hash *= primes[card]
  return hash

# Note, hands should be just contain kokushi card.
def kokushiHash(hands):
  hash = 1
  for card in hands:
    if card in kokushiList:
      hash *= kokushiList[card]
  return hash

