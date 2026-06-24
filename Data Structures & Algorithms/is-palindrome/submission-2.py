class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        rangeOfASCIINums = range(48, 58)
        rangeOfASCIIChars = range(65, 121)
        for char in s:
            if char != " " and (ord(char) in rangeOfASCIINums or ord(char) in rangeOfASCIIChars):
                newStr += char.lower()
        return newStr == newStr[::-1]