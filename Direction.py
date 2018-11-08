""" Direction """
def main():
    """ input number X Y """
    numx = int(input())
    numy = int(input())
    if numx == 0 and numy == 0:
        print("Origin")
    elif numx == 0 and numy > 0:
        print("North")
    elif numx == 0 and numy < 0:
        print("South")
    elif numx > 0 and numy > 0:
        print("Northeast")
    elif numx > 0 and numy < 0:
        print("Southeast")
    elif numx < 0 and numy > 0:
        print("Northwest")
    elif numx < 0 and numy < 0:
        print("Southwest")
    elif numx > 0 and numy == 0:
        print("East")
    else:
        print("West")

main()
