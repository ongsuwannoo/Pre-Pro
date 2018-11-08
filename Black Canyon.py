"""Black Canyon """
def funcinput():
    """input drink and cake"""
    drink = int(input())
    cake = int(input())
    count = (drink + cake) * 0.8
    return count

def main():
    """ main func """
    total = funcinput()
    count = total
    total = funcinput()
    count = count + total
    total = funcinput()
    count = count + total
    total = funcinput()
    count = count + total
    total = funcinput()
    count = count + total
    print("Total : %.2f Baht"%(count * 0.9))

main()
