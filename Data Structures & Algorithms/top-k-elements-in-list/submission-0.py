from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        c = Counter(nums)
        count = k
        insertIndex = -1

        while count > 0:
            largestElement = c.most_common(1)[0][0]
            ans.insert(insertIndex, largestElement)
            del c[largestElement]
            insertIndex -= 1
            count -= 1
        
        return ans
        
