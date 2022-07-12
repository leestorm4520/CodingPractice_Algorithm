nums=[1,2,3,4,5,6,7]
k=3
a=[0]*len(nums)
for i in range(len(nums)):
    a[(i+k)%len(nums)]=nums[i]
for i in range(len(nums)):
    nums[i]=a[i]
print(nums)

'''
Approach #1 Using Extra Array

We use an extra array in which we place every element of the array at its correct position i.e. the number at index ii in the original array is placed at the index (i+k)%(length of array)(i+k). Then, we copy the new array to the original one.

class Solution1:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i] #recycle

        for i in range(len(nums)):
            nums[i] = a[i]
Complexity Analysis

Time complexity : O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
Space complexity :O*(*n). Another array of the same size is used.
Approach #2 Using Cyclic Replacements


class Solution2:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1
Complexity Analysis

Time complexity : O(n). Only one pass is used.
Space complexity : O(1). Constant extra space is used.
Approach #4 Using Reverse
Algorithm

This approach is based on the fact that when we rotate the array k times, k%nk elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n-kn−kelements gives us the required result.

Let n=7n=7 and k=3k=3.

Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
class Solution4:
    def rotate(self, nums, k) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp 
            start += 1
            end -= 1
Complexity Analysis

Time complexity : O(n) .nnelements are reversed a total of three times.
Space complexity : O(1). No extra space is used.

'''