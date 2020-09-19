def OneOrZeroEditsAway(s1, s2):
    if s1 == s2:
        return True
    #1 replace away
    if len(s1) == len(s2):
        return checkOneReplace(s1, s2)
    #1 insert away
    if (len(s1)-1) == len(s2):
        return checkOneEdit(s1, s2)
    #1 remove away
    if (len(s2)-1) == len(s1):
        return checkOneEdit(s2, s1)
    return False

def checkOneReplace(s1, s2):
    diff = False
    for x in range(len(s1)):
        if s1[x] != s2[x]:
            if diff:
                return False #more than 1 difference
            diff = True
    return diff
    
def checkOneEdit(s1, s2): #s1 is longer
    idx1 = 0
    idx2 = 0
    while (idx1 < len(s1) and idx2 < len(s2)):
        if (s1[idx1] != s2[idx2]):
            if idx1 != idx2:
                return False
            idx1 += 1
        else:
            idx1 += 1
            idx2 += 1
    return True

print(OneOrZeroEditsAway("TEST", "TESTSS"))