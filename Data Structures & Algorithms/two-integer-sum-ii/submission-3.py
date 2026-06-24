

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while (l < r):
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if r != len(numbers) - 1:
                r += 1
            else:
                l += 1
                r = l + 1
               

       

        