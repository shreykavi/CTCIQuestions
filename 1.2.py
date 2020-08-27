def checkPermutation(s1, s2):
    if len(s2) != len(s1):
        return False

    for char in s1:
        s2 = s2.replace(char, "", 1)
    if len(s2) > 0:
        return False
    return True
print(checkPermutation("TETS", "TEST"))