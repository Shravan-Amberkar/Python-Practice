def sublist(l1,l2):  #sublist([2,2,3],[2,2,3,4,5])
    value=False
    if l1==[]: # empty list is a sublist
        return True
    elif len(l1)> len(l2): 
        return False
    else:
        for i in range(len(l1)):
            if l1[i]==l2[i]:
                value=True
                #print(value)
            else:
                value=False
                #print(value)
        return value
