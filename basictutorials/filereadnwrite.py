""" file read and write tutorials """
def main():
    """Test code"""
    alice = open('./alice.txt')
    alice_lines = alice.readlines()
    print alice_lines
    alice.close()

    output = open('./output.txt', 'w')
    output.writelines(['abc', 'cdc'])
    output.writelines(alice_lines)
    output.close()

    import os
    print os.getcwd()

    try:
        filepointer = open('nonexisting.file')
    except IOError, exception:
        print exception
    else:
        filepointer.close()

    alice = open('./alice.txt')
    alice_txt = alice.read()
    alice_lines = alice.readlines()
    alice.close()
    print len(alice_txt)
    print len(alice_lines)

    alice = open('./alice.txt')
    alice_lines = alice.readlines()
    alice_txt = alice.read()
    alice.close()
    print len(alice_txt)
    print len(alice_lines)

    try:
        output_file = open('./output.txt', 'w')
        output_file.write(3.14)
    except TypeError, type_error:
        print type_error
    else:
        output_file.close()

if __name__ == '__main__':
    main()
