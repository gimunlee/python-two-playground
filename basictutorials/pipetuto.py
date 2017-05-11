""" pipe tutorial """
import os

def main():
    """test code"""
    listing_cwd_content = 'dir'
    filep = os.popen(listing_cwd_content)
    print filep
    response = filep.read()
    stat = filep.close()
    print response
    print stat

if __name__ == "__main__":
    main()
