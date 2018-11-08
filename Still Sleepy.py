""" Still Sleepy """
def hhh():
    """ input h """
    hours = int(input())
    return hours
def mmm():
    """ input m """
    minute = int(input())
    return minute

def day():
    """ process """
    wakeuph = hhh()
    wakeupm = mmm()
    whwm = wakeuph * 60 + wakeupm
    ready = 40
    walk = 15
    tumjai = 10
    if whwm < 540:
        if whwm >= 450:
            tumjai = 0
        if whwm >= 465:
            ready -= 6
            tumjai = 0
        if whwm >= 480:
            walk -= 9
            tumjai = 0
        if whwm >= 495:
            ready -= 8
            tumjai = 0
        timeallm = walk + ready + tumjai
        timeh = timeallm // 60
        timem = timeallm % 60
        hours = wakeuph + timeh + ((wakeupm + timem) // 60)
        minutes = (wakeupm + timem) % 60
        print("%02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))"%\
            (wakeuph, wakeupm, hours, minutes, timeh, timem))
    if whwm >= 540:
        print("Continued sleeping")

day()
