""" List tutorials """
def main():
    """Test code"""
    li = [3, 2, 6]
    tail_li = [4, 5]

    #li.append(tailli)
    li.extend(tail_li)

    print li
    help(len)
    print dir(list)
    help(list.__add__)

    print sorted(li)
    print li
    li.reverse()
    print li
    li.sort()
    print li

    #List comprehension
    wood = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'.split()
    print wood
    print [list(x) for x in wood if len(x) == 5]

    #Generator ~~ lazy evaluation
    def generator(size):
        """sample generator"""
        i = 0
        while i < size:
            print 'i = %d' % i
            yield i
            i += 1
    for step in generator(5):
        print 'step = %d' % step

    #Generator expression
    tuple1 = tuple((x + 1 for x in range(3)))
    print tuple1

if __name__ == "__main__":
    main()
