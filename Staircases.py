""" Staircases """
def main():
    """ input n """
    nnn = int(input())
    inp = 0
    nn2 = 1
    num1 = str()
    while inp != nnn:
        num1 += ("*" * nn2)
        nn2 += 1
        inp += 1
        num1 += ("\n")
    print(num1)


def main2():
    for i in range(1, int(input())+1):
        print("*"*i)
main2()
