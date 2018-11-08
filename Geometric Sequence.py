""" Geometric Sequence """
def main():
    """ input a1 n r """
    aaa = float(input())
    count = int(input())
    rat = float(input())
    if rat != 0:
        num1 = 1
        while num1 <= count:
            print("%.2f"%(aaa), end=" ")
            aaa *= rat
            num1 += 1

main()
