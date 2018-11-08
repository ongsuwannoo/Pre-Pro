""" Election Chance """

def main():
    """get"""
    persent = int(input())
    years = int(input())
    process = int((1 - ((persent / 100) * (years - 2018))) * 100)
    process_2 = process * (process > 0)
    print(process_2, "%")

main()
