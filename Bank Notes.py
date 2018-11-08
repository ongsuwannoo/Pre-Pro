"""Bank Notes"""

def main():
    """get price"""
    price = int(input())
    number_t = ((price // 1000) * (price > 999))
    price_t = (number_t * 1000)
    price_h = (((price - price_t) // 100)) * 100
    number_fh = (price_h // 500) * (price_h > 499)
    price_fhc = ((price_h - 500) // 100) * (price_h > 500)
    number_h = (price_fhc + ((price_h // 100) * (price_h < 500)))
    price_te = (price - (price_t + price_h))
    number_ft = (price_te // 50) * (price_te > 49)
    price_ftc = (((price_te - 50)) * (price_te > 50)) + ((price_te) * (price_te < 50))
    number_tt = (price_ftc // 20)
    number_te = ((price_te == 10) + (price_te == 30) + (price_te == 60) + (price_te == 80))
    print(number_t)
    print(number_fh)
    print(number_h)
    print(number_ft)
    print(number_tt)
    print(number_te)

main()
