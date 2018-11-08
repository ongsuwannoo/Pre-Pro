""" Mysterious Number """
def main():
    """ input number """
    numt = float(input())
    num = float(input())
    prinall = str()
    if num == numt:
        print("Yeah!")
    else:
        while num != numt:
            if num > numt:
                prin = ("Too Much!")
            elif num < numt:
                prin = ("More!")
            prinall += prin + ("\n")
            num = float(input())
        if num == numt:
            print(prinall+"Yeah!")

main()
