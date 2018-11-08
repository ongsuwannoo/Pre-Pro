""" Popular """
def main():
    """ input str """
    word1 = input()
    word2 = input()
    word3 = input()
    word4 = input()
    word5 = input()
    yess = (("Yes" in word1) * 1) + (("Yes" in word2) * 1) + (("Yes" in word3) * 1)\
     + (("Yes" in word4) * 1) + (("Yes" in word5) * 1)
    if yess == 5:
        print("Superstar")
    elif yess == 4:
        print("Very Popular")
    elif yess == 3:
        print("Popular")
    elif yess >= 1:
        print("Ordinary Student")
    else:
        print("Invisible")

main()
