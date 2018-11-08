""" Number Digits """

def main():
    """get number 1-5"""
    number_1 = int(input())
    number_2 = int(input())
    number_3 = int(input())
    number_4 = int(input())
    number_5 = int(input())
    process_1 = (number_1 % 10)
    process_2 = ((number_2 % 100) // 10)
    process_3 = ((number_3 % 1000) // 100)
    process_4 = ((number_4 % 10000) // 1000)
    process_5 = ((number_5 % 100000) // 10000)
    process = (process_1 + process_2 + process_3 + process_4 + process_5)
    print("%i+%i+%i+%i+%i = %i"%(process_1, process_2, process_3, process_4, process_5, process))

main()
