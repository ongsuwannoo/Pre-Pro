""" Number Game """
def main():
    """ input numcoke numsaint numgunn """
    numcoke = int(input())
    nums1 = int(input())
    numg1 = int(input())
    nums2 = int(input())
    numg2 = int(input())
    nums3 = int(input())
    numg3 = int(input())
    numsa = nums1 + nums2 + nums3
    numga = numg1 + numg2 + numg3
    if numsa > numcoke:
        saint = numsa - numcoke
    elif numsa < numcoke:
        saint = numcoke - numsa
    if numga > numcoke:
        gunn = numga - numcoke
    elif numga < numcoke:
        gunn = numcoke - numga
    else:
        saint = numcoke
        gunn = numcoke
    if saint < gunn:
        print("Saint won!")
    elif gunn < saint:
        print("Gunn won!")
    else:
        print("Draw!")

main()
