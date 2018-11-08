""" Doubling """
def main():
    """ input num """
    num = int(input())
    i = 1
    while num >= 0:
        num -= 1
        print(i)
        i += i

main()
