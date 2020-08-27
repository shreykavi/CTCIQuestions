#Easy approach
def URLify(s):
    s = s.replace(" ", "%20")
    return s

print(URLify("THIS IS TEST"))
