class Solution:
    def validPalindrome(self, s: str) -> bool:
        listS = list(s)
        for i in range(len(listS)):
            c = listS.pop(i)
            strS = ("").join(listS)
            if strS == strS[::-1]:
                return True
            else:
                listS.insert(i, c)
        return False 
