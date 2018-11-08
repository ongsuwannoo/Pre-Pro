""" Pyramid """
def main():
    """ input n """
    nnn = int(input())
    nn3 = nnn
    inp = 0
    nn2 = 1
    num1 = str()
    while inp != nnn:
        num1 += ((" " * (nn3 - 1)) + ("*") * nn2)
        nn2 += 2
        inp += 1
        nn3 -= 1
        num1 += ("\n")
    print(num1)

main()
