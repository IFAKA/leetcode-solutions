class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Algorithm:
        # 1. Initialize answer array with 1s (length = len(nums)).
        # 2. First pass: Compute product of all elements to the left of each index.
        # 3. Second pass: Multiply by product of all elements to the right.
        # 4. Return answer.
        
        n = len(nums)
        answer = [1] * n
        
        # First pass: Compute left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Second pass: Multiply by right products
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer