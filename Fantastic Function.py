""" Fantastic Function """

def main():
    """"Main Function"""
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())
    print(myfunc())

def myfunc():
    """My function"""
    num = int(input())
    result = (num**3 + 2*num + 3) - (num**2 + 3*num + 2)
    return result

main()
