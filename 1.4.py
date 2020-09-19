# #Solution 1
# def isPalindromePermutation(s):
#     table = {}
#     for char in s:
#         if char in table:
#             table[char] += 1
#         else: 
#             table[char] = 1

#     odd_count = 0
#     for key in table:
#         if ((table[key] % 2) != 0):
#             odd_count += 1
#             if (odd_count > 1):
#                 return False
#     return True

# #Solution 2
# def isPalindromePermutation(s):
#     table = {}
#     odd_count = 0
#     for char in s:
#         if char in table:
#             table[char] += 1
#             if table[char] % 2 != 0:
#                 odd_count += 1
#             else:
#                 odd_count -= 1
#         else: 
#             table[char] = 1
#             odd_count += 1
#     return (odd_count <= 1)

#Solution 3
# odd = False
# even = True
def isPalindromePermutation(s):
    table = {}
    odd_count = 0
    for char in s:
        if char in table:
            table[char] = not table[char]
            if not table[char]:
                odd_count += 1
            else:
                odd_count -= 1
        else: 
            table[char] = False
            odd_count += 1
    return (odd_count <= 1)

print(isPalindromePermutation("TSSSAST"))