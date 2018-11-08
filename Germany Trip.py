""" Germany Trip """
def proc():
    """ process """
    import math as m
    numx1 = int(input())
    numy1 = int(input())
    numx2 = int(input())
    numy2 = int(input())
    numx3 = int(input())
    numy3 = int(input())
    numx4 = int(input())
    numy4 = int(input())
    numx5 = int(input())
    numy5 = int(input())
    result1 = m.sqrt(m.pow((numx2 - numx1), 2) + (m.pow((numy2 - numy1), 2)))
    result2 = m.sqrt(m.pow((numx3 - numx2), 2) + (m.pow((numy3 - numy2), 2)))
    result3 = m.sqrt(m.pow((numx4 - numx3), 2) + (m.pow((numy4 - numy3), 2)))
    result4 = m.sqrt(m.pow((numx5 - numx4), 2) + (m.pow((numy5 - numy4), 2)))
    print("%d"%(m.ceil(result1 + result2 + result3 + result4)))
proc()
