""" Sort """
def main():
    """ input num1-4 """
    num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    num1, num2, num3, num4 = myfunc(num1, num2, num3, num4)
    print("%d\n%d\n%d\n%d" % (num1, num2, num3, num4))

def myfunc(num1, num2, num3, num4):
    """ sorting """
    num1, num2 = max(num1, num2), min(num1, num2)
    num2, num3 = max(num2, num3), min(num2, num3)
    num3, num4 = max(num3, num4), min(num3, num4)
    return num1, num2, num3, num4

main()
