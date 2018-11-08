""" Choose Your Game """
def main():
    """ input money """
    num = float(input())
    if num >= 2100:
        num = num - 2100
        print("Detroit: Become Human")
    if num >= 1499:
        num = num - 1499
        print("Grand Theft Auto V")
    if num >= 1399:
        num = num - 1399
        print("Overwatch")
    if num >= 945:
        num = num - 945
        print("Minecraft: Java Edition")
    if num >= 315:
        num = num - 315
        print("Stardew Valley")

main()
