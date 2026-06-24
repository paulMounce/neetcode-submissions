from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        dictC = dict(c)
        for val in dictC.values():
            if val != 1:
                return True
        return False

"""
{"name": "Paul"}
"""
