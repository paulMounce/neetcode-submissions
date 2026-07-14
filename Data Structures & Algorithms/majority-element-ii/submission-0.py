from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        c = dict(Counter(nums))
        for key in c:
            if c[key] > len(nums) / 3:
                ans.append(key)
        return ans
        