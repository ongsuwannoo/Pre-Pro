""" Backward Skipping """
def main():
    """ input num,k """
    num = int(input())
    k = int(input())
    for i in range(num, -1, - k):
        print(i)

main()
