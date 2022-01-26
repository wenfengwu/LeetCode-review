# # You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# # Return any permutation of nums1 that maximizes its advantage with respect to nums2.

# Example 1:

# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:

# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]
 

# Constraints:

# 1 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 109

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        result = []
        #Generate a dictionary, value is a list
        counter = defaultdict(list)
        #sort array B in reverse order, then compare each value of A from the end of A
        for idx in sorted(B, reverse=True):
            #if the largest one form A is greater than B
            if A[-1] > idx: 
                #append into the dict array, key is the element in B
                counter[idx].append(A.pop())
        #traverse each element in B
        print(B)
        for idx in B:
            #if counter[idx] got something
            if counter[idx]:
                #take the value and append to result array
                result.append(counter[idx].pop())
            else:
                #otherwisw, take the value of array A append into result array
                result.append(A.pop())
        return result