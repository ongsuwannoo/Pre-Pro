""" Diamond """
def main():
    """ input n """
    rows = int(input())
    for i in range(1, int(rows/2)+1):
        for _ in range(int(rows/2)+1-i, 0, -1):
            print(' ', end='')
        for _ in range(2*i-1):
            print('*', end='')
        print()

    for i in range(int(rows/2)+1, 0, -1):
        for _ in range(int(rows/2)+1-i, 0, -1):
            print(' ', end='')
        for _ in range(2*i-1):
            print('*', end='')
        print()


def main2():
    num = int(input())
    for i in range(1, num//2+2):
        print(" "*(num//2+1-i)+"*"*(i*2-1))
    for i in range(1, num//2+1):
        print(" "*i + "*"*(num-(i*2)))

main2()
