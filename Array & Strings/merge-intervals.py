class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Algorithm:
        # 1. Sort intervals by start time.
        # 2. Initialize result with first interval.
        # 3. For each interval, if it overlaps with last result interval (start <= last_end),
        #    update last_end to max of current end and last_end.
        # 4. Else, append new interval to result.
        # 5. Return result.
        
        if len(intervals) <= 1:
            return intervals
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            if start <= last_end:
                # Overlap: update end of last interval
                result[-1][1] = max(last_end, end)
            else:
                # No overlap: append new interval
                result.append([start, end])
        
        return result