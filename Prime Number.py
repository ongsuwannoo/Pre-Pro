""" Prime Number """
def main():
    """ input number """
    num = int(input())
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print("Yes")
    else:
        print("No")

main()
