""" End of the world """
def main():
    """ input name devil brace """
    name = input()
    devil = int(input())
    brave = int(input())
    devil30 = devil * 0.3
    if brave > devil30:
        devil45 = devil - (devil * 0.45)
    else:
        devil45 = devil
    if "Justify yourself!" == name:
        devil20 = devil45 - (devil45 * 0.2)
    else:
        devil20 = devil45
    devilleft = devil20 - brave
    if devilleft <= 0:
        print("We saved the world!")
    elif devilleft > 1000:
        print("End of the world.")
    else:
        print("A great loss.")

main()
