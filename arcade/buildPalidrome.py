"""
Given a string, find the shortest possible string which can be achieved by
adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""

def buildPalindrome(st):
    length = len(st)
    for i in range(length):
        sub = st[i:length]  # removes first letter from string
        if sub == sub[::-1]:
            part = st[0:i]  # if sub is palindrome move what you removed above into part
            return st + part[::-1]  # add part to st and return

    return ""


print(buildPalindrome("abba"))
print(buildPalindrome("abcdc"))
