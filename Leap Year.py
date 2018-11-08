""" Leap Year """
def main():
    """ input """
    years = int(input())
    year1 = years % 4
    year2 = years % 100
    year3 = years % 400
    if years > 0:
        if year1 == 0:
            if year2 == 0:
                if year3 == 0:
                    print("%i is leap year."%(years))
                else:
                    print("%i is not leap year."%(years))
            else:
                print("%i is leap year."%(years))
        else:
            print("%i is not leap year."%(years))
    else:
        print("This year does not exist.")

main()
