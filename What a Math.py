""" What a Math """
def inputx():
    """ input x """
    num = float(input())
    return num

def inputa():
    """ input degrees """
    degrees = float(input())
    return degrees

def calcu():
    """ calculate """
    import math
    costx = inputx()
    costa = inputa()
    rad = (costa * (math.pi / 180))
    sqrta = math.sqrt(costa)
    asin6 = costa * (math.sqrt(3) / 2)
    suma = sqrta + asin6
    sqsua = math.sqrt(suma)
    a333 = costa**3
    a3sum = a333 + sqsua
    sqa3su = math.sqrt(a3sum)
    xca = costx * math.cos(rad)
    xdea = xca - sqa3su
    result = ((xdea > 0) * xdea * (-1)) + ((xdea < 0) * xdea)
    print(int(result))

calcu()
