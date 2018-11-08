""" Count Fast! """
def main(num):
    """ input """
    name1 = str(input())
    name2 = str(input())
    name3 = str(input())
    name4 = str(input())
    name5 = str(input())
    print("%s:%d#\t\t%s:%d#\t\t%s:%d#\t\t%s:%d#\t\t%s:%d#"%\
        (name1, num, name2, num+1, name3, num+2, name4, num+3, name5, num+4))
main(1)
main(6)
main(11)
main(16)
main(21)
main(26)
main(31)
main(36)
main(41)
main(46)
