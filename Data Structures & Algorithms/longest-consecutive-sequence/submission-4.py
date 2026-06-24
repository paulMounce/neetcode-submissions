

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        currentNum = 0
        longestSeq = []

        for num in setNums:
            currentNum = num
            currentSeq = []

            while currentNum in setNums:
                currentSeq.append(currentNum)
                currentNum += 1

            if len(currentSeq) > len(longestSeq):
                longestSeq = currentSeq

        return len(longestSeq)
"""
nums=[9,1,4,7,3,-1,0,5,8,-1,6]
sorted -> [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
""" 
                


