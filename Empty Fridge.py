""" Empty Fridge """
def main():
    """ input number """
    cola = int(input())
    tea = int(input())
    orenge = int(input())
    strawberry = int(input())
    milk = int(input())
    print("-Shopping List-")
    if cola < 12:
        num = 12 - cola
        print("Cola x%i"%(num))
    if tea < 16:
        num1 = 16 - tea
        print("Tea x%i"%(num1))
    if orenge < 20:
        num2 = 20 - orenge
        print("Orange Juice x%i"%(num2))
    if strawberry < 24:
        num3 = 24 - strawberry
        print("Strawberry Juice x%i"%(num3))
    if milk < 32:
        num4 = 32 - milk
        print("Milk x%i"%(num4))

main()
