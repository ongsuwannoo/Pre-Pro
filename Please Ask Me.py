""" Please Ask Me """
def main():
    """ input number """
    number = float(input())
    if number >= 8:
        print("Extremely Happy")
    elif number >= 4:
        print("Very Happy")
    elif number >= 1:
        print("Happy")
    else:
        print("Sad")
 
main()