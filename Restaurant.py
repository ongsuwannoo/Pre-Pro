""" Restaurant """

def main():
    """get price then process Service 10% Charge and vat 7%"""
    price = int(input())
    print("Service Charge : %.2f Baht"%(price * 0.10))
    print("VAT : %.2f Baht"%(price * 0.07))
    print("Total : %.2f Baht"%((price * 0.10) + (price * 0.07) + price))

main()
