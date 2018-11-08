""" Admission """
def ranks(rank):
    """ input rank"""
    if rank == "A":
        return 20000
    elif rank == "B":
        return 17500
    elif rank == "C":
        return 18000
    elif rank == "D":
        return 28250
    elif rank == "E":
        return 27000
    elif rank == "F":
        return 25000
    else:
        return ranks2(rank)

def ranks2(rank):
    """ rank """
    if rank == "G":
        return 21750
    elif rank == "H":
        return 22000

def main():
    """input score ad"""
    score = int(input())
    rank1 = input()
    rank2 = input()
    rank3 = input()
    rank4 = input()
    if score >= ranks(rank1):
        print(rank1)
    elif score >= ranks(rank2):
        print(rank2)
    elif score >= ranks(rank3):
        print(rank3)
    elif score >= ranks(rank4):
        print(rank4)
    else:
        print("None")

main()
