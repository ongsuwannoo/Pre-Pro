""" Did someone say something """
def main():
    """ input str """
    sentence = input()
    charl = input()
    print(check(sentence, charl))

def check(sentence, charl):
    """ check """
    if charl in sentence:
        return "Did someone say %s?" %charl
    return "That didn't work."

main()
