class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Algorithm:
        # 1. Handle edge cases (empty array or single number).
        # 2. Initialize the start of the first range with the first number.
        # 3. Iterate through the array, checking for gaps (non-consecutive numbers).
        # 4. When a gap is found or at the end, format the range ("a->b" or "a") and add to result.
        # 5. Update start for the next range and return the result.
        
        # Handle edge cases
        if not nums:
            return []
        
        result = []
        start = nums[0]  # Start of the current range
        
        for i in range(len(nums)):
            # Check if we're at the last number or a gap exists
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                # Format the range
                if start == nums[i]:
                    result.append(str(start))  # Single-number range
                else:
                    result.append(f"{start}->{nums[i]}")  # Multi-number range
                # Start new range if not at the end
                if i < len(nums) - 1:
                    start = nums[i + 1]
        
        return result