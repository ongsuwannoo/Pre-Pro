""" Perfect Pear """
def main():
    """ input """
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    maxx = max(num1, num2, num3)
    minn = min(num1, num2, num3)
    med = (num1 + num2 + num3) - (maxx + minn)
    print(med)

main()
