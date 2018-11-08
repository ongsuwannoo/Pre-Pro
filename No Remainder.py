""" No Remainder """
def main():
    """ input a,b """
    numa = int(input())
    numb = int(input())
    if numa != 0 and numb > 0:
        if numa > 0:
            while numa >= 1:
                dvi = numa % numb
                if dvi == 0:
                    print(numa)
                numa -= 1
        else:
            while numa <= -1:
                dvi = numa % numb
                if dvi == 0:
                    print(numa)
                numa += 1

main()
