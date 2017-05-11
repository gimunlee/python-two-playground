"""Tutorial for types"""
def main():
    """Test type tutorials"""
    print type('hello')
    print type(256)

    print int('1024')
    print int(3.14)

    print float('1.99')
    print float('1')
    print float(5)

    print str([1, 2, 3, 4])

    print list('Mary')
    print list((1, 2, 3, 4))

    print tuple('Mary')
    print tuple([1, 2, 3, 4])

if __name__ == '__main__':
    main()
