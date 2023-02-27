from random import *
from math import *

s = "coucou les gens"
s2 = s.replace('e', 'a', 1)
# print(s2)
s3 = s.split(' ', 1)
# print(s3)
s4 = "_".join(s3)
# print(s4)
# s.replace()
l = [1, 2, 3, 4, 5]
# print(l[3])
# print(l[3:4])
# print(l[3:5])
# *--------------------------------
# print(s[3:8])
# print(len(s))
# print(s[11:15])
# print(s[11:])
# print(s[:-4])
# print(s[::])

# *---------------------------------
# for letter in s:
#     print(letter)

value = 10
iterator = range(value)

# for n in iterator:
#     print(n, end='_')
# *------------------------------


def volume(cota, cotb, cotc):
    vol = cota*cotb*cotc
    # print(vol)
    return vol

# print(volume(1, 2, 3))


# AnyStr = TypeVar('AnyStr', str, bytes)


# def cone(r: AnyStr, h: AnyStr) -> AnyStr:
#     return 3.14*r*r*h/3


# print(cone(1, 2))
# *----------------------------------
# !imports
# print(random()*100)
# print(floor(random()*100)+1)
nmb_test = 10000
count = 0

for test in range(nmb_test):
    x = random()
    y = random()
    shoot = x*x+y*y
    if (shoot < 1):
        count = count+1

# *test PI calc
# *count is in 1/4 circle
# * count * 4 = circle and divide by number of throw
print(count*4/nmb_test)
