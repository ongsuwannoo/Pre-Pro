""" Any tax """
def main():
    """get price then process Service Charge 10% and vat 7%"""
    price = int(input())
    service_charge = price * 0.10
    service_charge_price = service_charge + price
    vat = service_charge_price * 0.07
    all_price = price + service_charge + vat
    print(int(all_price))

main()
