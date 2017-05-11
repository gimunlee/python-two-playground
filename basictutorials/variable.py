""" variables tutorial """
X = 5
Y = 'red'
Y2 = "red"

print Y
print Y2
print '%s and %s are same? : %s %s' % (Y, Y2, Y == Y2, Y is Y2)
print (3, 4)
print 3, 4
print '%d' % 1
A = [1]
B = A
print A == B
print A is B
C = A[:]
print A == C
print A is C
