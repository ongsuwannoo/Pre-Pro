""" Split Function """
def main():
    """ input X """
    import math
    numx = float(input())
    if numx < 100:
        radians = numx -10
        degrees = radians * (math.pi / 180)
        result = 2 * math.sin(degrees)
        print("%.2f" %(result))
    elif numx == 100:
        result = (math.sqrt(numx)) / 5
        print("%.2f" %(result))
    if numx > 100:
        result = math.log10(numx)
        print("%.2f" %(result))

main()
