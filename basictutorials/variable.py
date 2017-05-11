""" variables tutorial """
x = 5
y = 'red'
y2 = "red"

print y
print y2
print '%s and %s are same? : %s %s' % (y, y2, y == y2, y is y2)
print (3, 4)
print 3, 4
print '%d' % 1
a = [1]
b = a
print a == b
print a is b
c = a[:]
print a == c
print a is c
