__author__ = 'candyfeline'

import card as c

# Evaluate hands with hash.

# Definitions.
bigPrime = 86028121
doi = [2**2, 3**2, 5**2, 7**2, 11**2, 13**2, 17**2, 19**2, 23**2]
ko = [2**3, 3**3, 5**3, 7**3, 11**3, 13**3, 17**3, 19**3, 23**3]
jun = [2*3*5, 3*5*7, 5*7*11, 7*11*13, 11*13*17, 13*17*19, 17*19*23]
mentsu = ko + jun
linkTwo = [2*3, 3*5, 5*7, 7*11, 11*13, 13*17, 17*19, 19*23]
kan = [2*5, 3*7, 5*11, 7*13, 11*17, 13*19, 17*23]
datsu = c.primeList + doi + linkTwo + kan

noten = 0
tenhai = 1
agari = 2


def judgeWithoutDoi(hash, dictW, dictWo):
  if hash in dictWo:
    return dictWo[hash]
  else:
    # if there is no card
    if hash == 1:
      judgement = agari
    # if there is a tatsu left
    elif hash in datsu:
      judgement = tenhai
    else:
      left = [judgeWithoutDoi(hash/test, dictW, dictWo)
              for test in mentsu if hash % test == 0]
      judgement = noten if not left else max(left)
    dictWo[hash] = judgement
    return judgement

def judgeWithDoi(hash, dictW, dictWo):
  if hash in dictW:
    return dictW[hash]
  else:
    # if there is no card
    if hash == 1:
      judgement = agari
    # if there is a doitsu left
    elif hash in doi:
      judgement = agari
    # otherwise, we find a doitsu.
    else:
      leftSearchDoi = [judgeWithoutDoi(hash/test, dictW, dictWo)
                        for test in doi if hash % test == 0]
      leftSearchCard = [judgeWithoutDoi(hash/test, dictW, dictWo) - 1
                        for test in c.primeList if hash % test == 0]
      leftSearchCard = [0 if x < 0 else x for x in leftSearchCard]
      left = leftSearchDoi + leftSearchCard
      judgement = noten if not left else max(left)
    dictWo[hash] = judgement
    return judgement

def judgeKokushi(kokushiHash):
  fullKokushi = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41
  kokushiAgari = [fullKokushi * card for card in c.primeKokushi]
  kokushiTenhai = set([fullKokushi]) + set([fullKokushi / lackCard * pairCard
                                          for lackCard in c.primeKokushi
                                          for pairCard in c.primeKokushi])
  if (kokushiHash in kokushiTenhai):
    return tenhai
  elif (kokushiHash in kokushiAgari):
    return agari
  else:
    return noten
