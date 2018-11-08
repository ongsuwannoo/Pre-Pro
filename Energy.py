"""Energy"""

def main():
    """get distance(km) and energy(cal) then process after print result"""
    distance = float(input())
    cal = int(input())
    distance_km = distance * 1000
    cal_process = cal * 10
    print(int(distance_km / cal_process) + (distance_km / cal_process%1 > 0))

main()
