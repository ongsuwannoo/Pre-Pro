""" Alpha Signal """
def main():
    """ input cha """
    cha = str.lower(input())
    for i in cha:
        cha_ord = ord(i) - 96
        ast = ("*" * cha_ord)
        print(ast)

main()
