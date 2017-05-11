"""Regular Expression tutorial"""
import re

def main():
    """Test code"""
    wood = 'How much wood would a woodchuck chuck?'
    print re.findall('wo\\w+', wood)
    print re.findall(r'wo\w+', wood)

    re_compiled = re.compile(r'\w+ou\w+')
    print re_compiled.findall(wood)

if __name__ == "__main__":
    main()
    