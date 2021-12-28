# # Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# # Example 1:

# # Input: nums1 = [1,2,2,1], nums2 = [2,2]
# # Output: [2,2]
# # Example 2:

# # Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# # Output: [4,9]
# # Explanation: [9,4] is also accepted.
 

# # Constraints:

# # 1 <= nums1.length, nums2.length <= 1000
# # 0 <= nums1[i], nums2[i] <= 1000
 

# # Follow up:

# # What if the given array is already sorted? How would you optimize your algorithm?
# # What if nums1's size is small compared to nums2's size? Which algorithm is better?
# # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# # Use dictionary
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         dic1 = {};
#         tempArr = [];
#         for num in nums1:
#             dic1[num] = dic1.get(num, 0) + 1
#         for elem in nums2:
#             if elem in dic1 and dic1[elem] > 0:
#                 tempArr.append(elem)
#                 dic1[elem] -= 1
                
#         return tempArr

# # use two pointers
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1 = sorted(nums1)
#         nums2 = sorted(nums2)
        
#         p1 = 0
#         p2=0
#         tempArr = []
        
#         while(p1<len(nums1) and p2<len(nums2)):
#             if(nums1[p1] > nums2[p2]):
#                 p2 += 1
#             elif(nums1[p1] < nums2[p2]):
#                 p1 += 1
#             else:
#                 tempArr.append(nums1[p1])
#                 p2 += 1
#                 p1 += 1
                
#         return tempArr

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        left = 1
        right = n
        while left <= right:
            m = (left + right) // 2
            if isBadVersion(m) == False:
                left = m+1
            else:
                right = m-1
                
        return left