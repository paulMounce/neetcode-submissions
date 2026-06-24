class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += string + "\n"
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedList = []
        singleStr = ""
        for char in s:
            if char != "\n":
                singleStr += char
            else:
                decodedList.append(singleStr)
                singleStr = ""
        return decodedList
       