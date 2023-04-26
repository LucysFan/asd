from functools import partial

import pandas as pd


throw = lambda facet, iter : [pd.np.random.randint(1, facet + 1) for i in range(iter)]

while (facet := int(input("Input facet >>> "))) not in [4, 8, 10, 12]:
  print("facet can only be 4, 8, 10 or 12")
iter = int(input("How many times throw? >>> "))

series = pd.Series(partial(throw, facet, iter)())
print(f"You threw {facet}-facet cube {iter} times and got \n{series.value_counts()}")

#2
from functools import partial

import pandas as pd
import censusname
from random import randint

students, honours, good = map(int, input("How many students there should be?\n         honours\n         good?\n").split(' '))
others = students - honours - good

_miniData = lambda x, y, z : {censusname.generate(nameformat = '{surname}, {given}') : [x, y, z]}

data = {}
for student in range(honours):
  data |= _miniData(5, 5, 5)
for student in range(good):

  while 4 not in (marks := [randint(4,5), randint(4,5), randint(4,5)]):
    pass
  data |= _miniData(marks[0], marks[1], marks[2])

_func = partial(_miniData)

for student in range(others):
  flag = 1
  marks = [randint(0,5), randint(0,5), randint(0,5)]
  while flag:
    for mark in marks:
      match mark:
        case 3 | 2 | 1| 0:
          flag *= 0
        case _:
          flag *= 1
  data |= _miniData(marks[0], marks[1], marks[2])

_help = partial(lambda x: data.values()[x])

frame = {'Students' : [k for k in data.keys()], 
         'Disc1'    : [i for i in _help(0)]   ,
         'Disc2'    : [i for i in _help(1)]   ,
         'Disc3'    : [i for i in _help(3)]}

dFrame = pd.DataFrame.from_dict(frame)
print(dFrame)

#4
from functools import reduce

from random import randint


manifold = [randint(-10_000, 10_000) for _ in range(100_000)]
print(reduce(lambda x, y: x*y == 0, mainifold))