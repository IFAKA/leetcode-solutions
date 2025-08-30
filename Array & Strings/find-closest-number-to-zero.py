class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # define the smallest as the first element
        # iterate over the nums
        # ask if smallest is smaller than current using absolute value
        #   if smallest then
        #       if is equal then get the greater one and update smallest
        #       else update the smallest 
        #   else skip it

        if len(nums) == 1:
            return nums[0]

        smallest = nums[0]

        for num in nums[1:]:
            if abs(num) == abs(smallest):
                smallest = max(num, smallest)
            elif abs(num) < abs(smallest):
                smallest = num

        return smallest