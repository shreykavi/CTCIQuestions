def allUniqueString(s):
    table = {}
    for letter in s:
        if letter in table:
            return False
        table[letter] = 1
    return True

print(allUniqueString('uniqe'))