""" Login """
def str1():
    """ input user """
    user = input()
    return user

def str2():
    """ input password """
    password = len(input())
    return password

def myfunc():
    """ print user password """
    print("username : %s\npassword : %s"%(str1(), str2() * "*"))

myfunc()
