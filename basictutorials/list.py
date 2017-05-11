""" List tutorials """
def main():
    """Test code"""
    lis = [3, 2, 6]
    tail_lis = [4, 5]

    #li.append(tailli)
    lis.extend(tail_lis)

    print lis
    help(len)
    print dir(list)
    help(list.__add__)

    print sorted(lis)
    print lis
    lis.reverse()
    print lis
    lis.sort()
    print lis

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

    print any([0, 0, 1])
    print any([0, 0, False])

    print all([0, 1, 1])
    print all([True, 1])

if __name__ == "__main__":
    main()
