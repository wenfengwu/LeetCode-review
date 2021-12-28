# 看具体的例子，1 2 3 4 5，k = 2。

# 转换后最终变成 4 5 1 2 3。

# 其实可以分三步完成。

# 整体逆序 5 4 3 2 1 。

# 前 k 个再逆序 4 5 3 2 1。

# 后边的再逆序 4 5 1 2 3

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
            
        def twopt(arr, i, j):
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
        
        if k > len(nums):
            k %= len(nums)
            
        if (k > 0):
            twopt(nums, 0, len(nums) - 1)  # rotate entire array
            twopt(nums, 0, k - 1)          # rotate array upto k elements
            twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reminder = k % len(nums)
        if reminder == 0:
            return;
        for i in range(0, reminder):
            nums.insert(0,nums.pop())
        return;