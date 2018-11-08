"""Time Converter"""
def main():
    """get second"""
    distance = float(input())
    velocity = int(input())
    times_h = ((distance * 1000) / velocity) // 3600
    times_m = (((distance * 1000) / velocity) % 3600) // 60
    times_s = (((distance * 1000) / velocity) % 3600) % 60
    print("%i Hour(s) %i Minute(s) %i Second(s)"%(times_h, times_m, times_s))

main()
