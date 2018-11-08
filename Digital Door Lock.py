""" Digital Door Lock """
def main():
    """input S E -1 """
    num1 = 0
    num = ""
    sta = ""
    while num != "-1":
        num = input()
        if num == 'S':
            sta = 1
        elif num == 'E' and sta == 1:
            num1 += 1
            sta = 0
    print(num1)
main()
