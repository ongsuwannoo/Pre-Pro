""" Average """
def main():
    """ input n,k """
    num = int(input())
    num1 = 1
    weightall = 0
    while num1 <= num:
        weight = float(input())
        weightall += weight
        num1 += 1
    average = weightall / num
    print("Average is %.2f"%(average))

main()
