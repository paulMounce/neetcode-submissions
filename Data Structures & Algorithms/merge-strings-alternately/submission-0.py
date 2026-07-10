class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        cCount = 0
        wordToAppend = word2
        output = ""
        if len(word1) <= len(word2):
            cCount = len(word1)
        else:
            cCount = len(word2)
            wordToAppend = word1
        for i in range(cCount):
            output += (word1[i] + word2[i])
        if wordToAppend == word2:
            output += word2[len(word1):]
        else:
            output += word1[len(word2):]
        return output