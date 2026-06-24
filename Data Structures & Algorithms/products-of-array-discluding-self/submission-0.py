class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listProducts = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if len(listProducts) == i and i == j:
                    continue
                product *= nums[j]
            listProducts.append(product)
            product = 1
        return listProducts    
        