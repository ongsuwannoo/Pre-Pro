""" Is This Calculus? """
def input1():
    """ input 1 """
    num = float(input())
    return num

def input2():
    """ input 2 """
    num = float(input())
    return num

def myfunc():
    """ process """
    inputx = input1()
    inputy = input2()
    maxx = max(inputx, inputy)
    minn = min(inputx, inputy)
    result = (((maxx**3) / 3) + maxx) - (((minn**3) / 3) + minn)
    print("%.2f"%(result))

myfunc()
