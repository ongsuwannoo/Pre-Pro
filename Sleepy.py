""" Sleepy """
def hhh():
    """ input h """
    hours = int(input())
    return hours
def mmm():
    """ input m """
    minute = int(input())
    return minute

def lll():
    """ input l """
    level = int(input())
    return level

def day():
    """ process """
    wakeuph = hhh()
    wakeupm = mmm()
    level = lll()
    tumjai = 10
    ready = 40
    walk = 15
    levelall = (tumjai + level) + (ready + (5 * level))
    timeallm = walk + levelall
    timeh = timeallm // 60
    timem = timeallm % 60
    hours = wakeuph + timeh + ((wakeupm + timem) // 60)
    minutes = (wakeupm + timem) % 60
    ppp = ("%02i:%02i - %02i:%02i (Time Used: %i Hour(s) %i Minute(s))"%\
        (wakeuph, wakeupm, hours, minutes, timeh, timem))
    return ppp

def printday():
    """print """
    day1 = day()
    day2 = day()
    day3 = day()
    day4 = day()
    day5 = day()
    day6 = day()
    day7 = day()
    day8 = day()
    day9 = day()
    day10 = day()
    print("[Day 01]", day1)
    print("[Day 02]", day2)
    print("[Day 03]", day3)
    print("[Day 04]", day4)
    print("[Day 05]", day5)
    print("[Day 06]", day6)
    print("[Day 07]", day7)
    print("[Day 08]", day8)
    print("[Day 09]", day9)
    print("[Day 10]", day10)

printday()
