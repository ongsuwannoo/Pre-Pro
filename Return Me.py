""" Return Me """

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
    result = num**4 - num**3 + num**2 - num
    return result

main()
