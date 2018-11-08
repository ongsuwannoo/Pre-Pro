"""balloon game"""

def injack():
    """ input jack """
    jackin = int(input())
    return jackin
def inrew():
    """ input rew """
    rewin = int(input())
    return rewin
def inpok():
    """ input pok """
    pokin = int(input())
    return pokin
def infight():
    """ input fight """
    fightin = int(input())
    return fightin
def injub():
    """ input jub """
    jubin = int(input())
    return jubin

def jack():
    """ result jack """
    jackout = injack()
    if jackout == 10:
        jackout = str("P'Jack won a large teddy bear.")
    elif jackout >= 8:
        jackout = str("P'Jack won a teddy bear.")
    elif jackout >= 6:
        jackout = str("P'Jack won a key chain.")
    elif jackout >= 4:
        jackout = str("P'Jack won a notebook.")
    elif jackout >= 1:
        jackout = str("P'Jack won a pen.")
    else:
        jackout = str("P'Jack won nothing.")
    return jackout

def rew():
    """ result rew """
    rewout = inrew()
    if rewout == 10:
        rewout = str("P'Rew won a large teddy bear.")
    elif rewout >= 8:
        rewout = str("P'Rew won a teddy bear.")
    elif rewout >= 6:
        rewout = str("P'Rew won a key chain.")
    elif rewout >= 4:
        rewout = str("P'Rew won a notebook.")
    elif rewout >= 1:
        rewout = str("P'Rew won a pen.")
    else:
        rewout = str("P'Rew won nothing.")
    return rewout

def pok():
    """ result pok """
    pokout = inpok()
    if pokout == 10:
        pokout = str("P'Pok won a large teddy bear.")
    elif pokout >= 8:
        pokout = str("P'Pok won a teddy bear.")
    elif pokout >= 6:
        pokout = str("P'Pok won a key chain.")
    elif pokout >= 4:
        pokout = str("P'Pok won a notebook.")
    elif pokout >= 1:
        pokout = str("P'Pok won a pen.")
    else:
        pokout = str("P'Pok won nothing.")
    return pokout

def fight():
    """ result fight """
    fightout = infight()
    if fightout == 10:
        fightout = str("P'Fight won a large teddy bear.")
    elif fightout >= 8:
        fightout = str("P'Fight won a teddy bear.")
    elif fightout >= 6:
        fightout = str("P'Fight won a key chain.")
    elif fightout >= 4:
        fightout = str("P'Fight won a notebook.")
    elif fightout >= 1:
        fightout = str("P'Fight won a pen.")
    else:
        fightout = str("P'Fight won nothing.")
    return fightout

def jub():
    """ result jub """
    jubout = injub()
    if jubout == 10:
        jubout = str("P'Jub won a large teddy bear.")
    elif jubout >= 8:
        jubout = str("P'Jub won a teddy bear.")
    elif jubout >= 6:
        jubout = str("P'Jub won a key chain.")
    elif jubout >= 4:
        jubout = str("P'Jub won a notebook.")
    elif jubout >= 1:
        jubout = str("P'Jub won a pen.")
    else:
        jubout = str("P'Jub won nothing.")
    return jubout

def printall():
    """ print all """
    jack_ = jack()
    rew_ = rew()
    pok_ = pok()
    fight_ = fight()
    jub_ = jub()
    print(jack_)
    print(rew_)
    print(pok_)
    print(fight_)
    print(jub_)

printall()
