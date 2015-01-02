import handHash as h
import card as c

__author__ = 'candyfeline'

dt = {}
df = {}

print(h.judgeWithoutDoi(c.cardHash([1, 2, 3, 3, 5]), dt, df)) # Should give tenhai
# Check 9-len.
dt = {}
df = {}
print(h.judgeWithoutDoi(c.cardHash([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]), dt, df)) # Should give tenhai
dt = {}
df = {}
print(h.judgeWithDoi(c.cardHash([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]), dt, df)) # Should give tenhai
dt = {}
df = {}
print(h.judgeWithDoi(c.cardHash([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 4]), dt, df)) # Should give agari
print(h.judgeWithoutDoi(c.cardHash([1, 1, 2, 4, 7, 9]), dt, df)) # should give noten
print(h.judgeWithDoi(c.cardHash([3, 7, 8, 9]), dt, df)) # Should be tenhai
dt = {}
df = {}
print(h.judgeWithDoi(c.cardHash([1, 2, 2, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 8]), dt, df)) # Should give noten
# TODO To implement the test.
# print(h.judgeKokushi())
