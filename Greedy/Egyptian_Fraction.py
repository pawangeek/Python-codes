# @Date:   2020-05-02T17:47:55+05:30
# @Last modified time: 2020-05-03T14:08:37+05:30

# 6/14 is 1/3 + 1/11 + 1/231

import math
ef = []

nr = 6
dr = 14

# while loop runs until fraction becomes 0 i.e, numerator becomes 0
while nr != 0:

    # taking ceiling
    x = math.ceil(dr / nr)

    # storing value in ef list
    ef.append(x)

    # updating new nr and dr
    nr = x * nr - dr
    dr = dr * x

for i in ef:
    print('1/{0}'.format(i),end=' ')
