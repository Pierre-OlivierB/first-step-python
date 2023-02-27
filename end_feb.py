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


print(volume(1, 2, 3))
