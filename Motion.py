""" Motion """
def inputu():
    """ input u """
    num = float(input())
    return num

def inputr():
    """ input degrees """
    import math
    degrees = float(input())
    rad = degrees * (math.pi / 180)
    return rad

def calcu():
    """ calculate """
    import math
    velocity = inputu()
    radius = inputr()
    times = (2 * (velocity * math.sin(radius))) / 9.8
    height = (velocity**2) * (math.sin(radius)**2) / (2 * 9.8)
    rangee = (velocity**2) * (math.sin(2 * radius)) / 9.8
    print("t = %.2f"%(times))
    print("H = %.2f"%(height))
    print("R = %.2f"%(rangee))

calcu()
