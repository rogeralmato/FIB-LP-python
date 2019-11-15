from functools import reduce


def myLength(L):
     return reduce(lambda ac,y: ac+y ,list(map(lambda x: 1, L)),0)


def myMaximum(L):
    return reduce(lambda max,y: max if y < max else y,L)


print(myMaximum(['josep', 'jordi', 'albert']))