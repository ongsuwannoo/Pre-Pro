""" Arithmetic Sequence  """
def main():
    """ input a1 n d """
    aaa = int(input())
    count = int(input())
    dif = int(input())
    num1 = 1
    while num1 <= count:
        print(aaa, end=" ")
        aaa += dif
        num1 += 1

main()
