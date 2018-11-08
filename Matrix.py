""" Matrix """
def main():
    """ input n """
    nnn = int(input())
    squa = nnn**2
    inp = 0
    nn2 = 0
    num1 = str()
    while nn2 <= squa and inp != squa:
        num = str(input())
        num1 += ("%s "%num)
        inp += 1
        nn2 += 1
        if nn2 == nnn:
            num1 += ("\n")
            nn2 = 0
    print(num1)

main()
