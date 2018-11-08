""" Another Staircases """
def main():
    """ input n """
    nnn = int(input())
    nn3 = nnn
    inp = 0
    nn2 = 1
    num1 = str()
    while inp != nnn:
        num1 += ((" " * (nn3 - 1)) + ("*") * nn2)
        nn2 += 1
        inp += 1
        nn3 -= 1
        num1 += ("\n")
    print(num1)

def main2():
    num = int(input())
    for i in range(1, num+1):
        print(" " * (num - i) + "*" * (i))
main2()
