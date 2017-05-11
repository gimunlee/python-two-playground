"""String methods tutorial"""
def main():
    """Main function"""
    print 'school'.startswith('sc')
    print 'school'.endswith('ol')
    print 'colorless green ideas sleep furiously'.count('ee')

    print 'Do not enter'.upper()
    print 'Do not enter'.lower()

    print 'do not enter'.capitalize()
    print 'do not enter'.title()

    mary = 'Mary had a little lamb'
    print mary.replace('a', 'xx')
    print mary

    hello_with_white_spaces = '  \t hello \n\tworld\n \n'
    print hello_with_white_spaces.strip()

    print 'green ideas'.index('id')
    print 'green ideas'.rindex('e')

    try:
        print 'green'.index('a')
    except ValueError, exception:
        print exception
    print 'green'.find('a')

    print 'iPad'.isalpha()
    print 'co-operate'.isalpha()
    print 'iphone4'.isalnum()
    print 'iphone-4'.isalnum()

    print mary.split()
    print mary.split('l')

    print list(mary)
    print '-'.join(list(mary))

if __name__ == '__main__':
    main()
