def main():
    size = int(input())
    result = area(int(input()), int(input()))
    print("Area = %d" %(result))
    box(size)

def box(size):
    print("*%s*"%("*" * size))
    print("*%s*\n"%(" " * size) * size, end="")
    print("*%s*"%("*" * size))

def area(width, hight):
    return width * hight

main()
