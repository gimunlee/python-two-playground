""" list tutorials """

LI = [3, 2, 6]
TAIL_LI = [4, 5]

#li.append(tailLi)
LI.extend(TAIL_LI)

print LI
help(len)
print dir(list)
help(list.__add__)

print sorted(LI)
print LI
LI.reverse()
print LI
LI.sort()
print LI
