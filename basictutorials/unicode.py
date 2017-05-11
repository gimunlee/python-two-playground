"""Unicode tutorial"""
def main():
    """Test code"""
    print '\x4D'
    print '\x4D' == 'M'

    print type('M')
    print type(u'M')
    print type(u'\u004D')
    print type(u'\U0000004D')
    print 'M' == u'M' == u'\u004D' == u'\U0000004D'

if __name__ == '__main__':
    main()
