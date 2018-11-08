""" Skipping """
def main():
    """ input n,k """
    num = int(input())
    k = int(input())
    for i in range(1, num+1, k):
        print(i)

main()
