__author__ = 'candyfeline'

import handHash as te
import card

linkTwoLeft = [5,        # 1 2 -> 3
               [2, 7],   # 2 3 -> 1 4
               [3, 11],  # 3 4 -> 2 5
               [5, 13],  # 4 5 -> 3 6
               [7, 17],  # 5 6 -> 4 7
               [11, 19], # 6 7 -> 5 8
               [13, 23], # 7 8 -> 6 9
               17        # 8 9 -> 7
              ]

# If there is a doi not for the pair, we need make it a ko.
doiLeft = card.primeList
# To make a single a pair, it is best to find it an alter ego.
singleLeft = card.primeList

kanLeft = [5,   # 1 3 -> 2
           7,   # 2...
           11,  # 3...
           13,  # 4...
           17,  # 5...
           19,  # 6...
           23  # 7...
           ]

shanponMachi = 1
kanchanMachi = 2
penchanMachi = 3
ryanmenMachi = 4
dankiMachi = 5
specialMachi = 10

# TODO  Use judgeWithoutDoi to use Tenpai.
# These functions are built on a premise that the hand is already tenpai.

def machiWithoutDoi(hash, dictW, dictWo):
  pass

def machiWithDoi(hash, dictW, dictWo):
  pass

def machiKokushi(kokushiHash):
  fullKokushi = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41
  machiKokushi = [
                   [[1], [], [], []],
                   [[9], [], [], []],
                   [[], [1], [], []],
                   [[], [9], [], []],
                   [[], [], [1], []],
                   [[], [], [9], []],
                   [[], [], [], [1]],
                   [[], [], [], [2]],
                   [[], [], [], [3]],
                   [[], [], [], [4]],
                   [[], [], [], [5]],
                   [[], [], [], [6]],
                   [[], [], [], [7]],
                 ]
  kokushiOneTenhai = {kokushiHash: [dankiMachi, machiKokushi[iLack]]
                          for iLack in xrange(13)
                          for pairCard in card.primeKokushi
                          if (kokushiHash % pairCard == 0) and
                             (kokushiHash / pairCard * card.primeKokushi[iLack]==fullKokushi)}
  # 13 Men.
  if (kokushiHash == fullKokushi):
    return [specialMachi, [[1, 9] * 3, range(0, 7)]]
  else:
    return [dankiMachi, kokushiOneTenhai[kokushiHash]]
