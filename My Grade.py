""" My Grade """
def main():
    """ input number """
    number = float(input())
    if number >= 90:
        print("A")
    elif number >= 80:
        print("B+")
    elif number >= 75:
        print("B")
    elif number >= 67:
        print("C+")
    elif number >= 50:
        print("C")
    elif number >= 40:
        print("D+")
    elif number >= 30:
        print("D")
    else:
        print("F")

main()
