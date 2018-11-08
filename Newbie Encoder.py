""" Newbie Encoder """

def inputcha():
    """ input """
    cha_ord = ord(str(input()))
    cha = (cha_ord - ((cha_ord == 90) * 26) - ((cha_ord == 122) * 26))
    return cha

def outputcha():
    """ output """
    cha_chr = chr(inputcha() + 1)
    print(cha_chr)

outputcha()
