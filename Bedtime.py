""" Bedtime """
def main():
    """ input time """
    h_sleep = int(input())
    m_sleep = int(input())
    h_wake = int(input())
    m_wake = int(input())
    times_sleep = h_sleep * 60 + m_sleep
    times_wake = h_wake * 60 + m_wake
    if times_sleep >= times_wake:
        times_wake += 24 * 60
    times = abs(times_sleep - times_wake)
    if times < 420:
        print("Not enough")
    elif times >= 420 and times < 600:
        print("Enough")
    elif times >= 600:
        print("Too much")

main()
