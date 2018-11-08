""" My Balls """
def line():
    """ input Diameter"""
    import math
    radius = float(input()) / 2
    area = 4 * math.pi * radius**2
    volume = (4 / 3) * math.pi * radius**3
    print("A = %.3f"%(area))
    print("V = %.3f"%(volume))

line()
