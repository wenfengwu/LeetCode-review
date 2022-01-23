# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: 
            return []
        # sort by the first element of each sub list
        intervals = sorted(intervals, key = lambda x: x[0]) 
        # add the first element into result
        res = [intervals[0]] 
        
        # check if it is overlap between current and result
        for current in intervals[1:]: 
            # if over lap, merge
            if current[0] <= res[-1][1]: 
                res[-1][1] = max(current[1], res[-1][1]) 
            else: 
                # if not, add current into result
                res.append(current) 
        return res 