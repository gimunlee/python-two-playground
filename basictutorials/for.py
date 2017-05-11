""" for loop tutorial """
THEMOTTO = ['you', 'only', 'live', 'once', '(YOLO)']
print THEMOTTO
for word in THEMOTTO:
    print word
    print len(word)

for letter in 'hello':
    print letter

"""
import random
t = [100]
for step in t:
    if step > 98:
        t.insert(0, random.randint(0, 100))
        t.insert(0, random.randint(0, 100))
        t.append(random.randint(0, 100))
    print t
"""
