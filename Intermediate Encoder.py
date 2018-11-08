""" Intermediate Encoder """
def outputcha():
    """ output cha """
    cha = ord(str(input()))
    if cha <= 90:
        if cha < 71:
            cha = (cha + 20)
        elif cha < 91:
            cha = (cha - 6)
    elif cha <= 122:
        if cha < 103:
            cha = (cha + 20)
        elif cha < 123:
            cha = (cha - 6)

    print(chr(cha))

outputcha()
