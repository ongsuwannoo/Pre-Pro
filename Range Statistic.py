""" Range Statistic """
def main():
    """ input n """
    nnn = int(input())
    if nnn > 0:
        maxx = int(input())
        minn = maxx
        for _ in range(1, nnn, 1):
            num1 = int(input())
            if num1 > maxx:
                maxx = num1
            if num1 < minn:
                minn = num1
    anss = maxx - minn
    print(anss)
main()
