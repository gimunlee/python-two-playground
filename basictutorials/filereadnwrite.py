""" file read and write tutorials """

ALICE = open('./alice.txt')
ALICE_LINES = ALICE.readlines()
print ALICE_LINES
ALICE.close()

OUTPUT = open('./output.txt', 'w')
OUTPUT.writelines(['abc','cdc'])
OUTPUT.writelines(ALICE_LINES)
OUTPUT.close()
