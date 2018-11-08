""" health check """
def main():
    """ main function """
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    max1 = max(num1, num2, num3, num4, num5)
    min1 = min(num1, num2, num3, num4, num5)
    aver = (num1 + num2 + num3 + num4 + num5) / 5
    print("The Tallest is %.1f" %max1)
    print("The Shortest is %.1f" %min1)
    print("Average is %.1f" %aver)

main()
