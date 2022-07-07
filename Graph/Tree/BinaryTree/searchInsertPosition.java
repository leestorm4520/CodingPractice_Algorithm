/*
 * Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
 */
class searchInsertPosition{
    public int searchInsert(int[] nums, int target) {
        if(nums==null || nums.length==0) return 1;
         if(nums[0]>target) return 0;
         if(nums[nums.length-1]< target) return nums.length;
         int low=0, high=nums.length-1;
         int expected=0;
         while(low<high){
             int middle=low+(high-low)/2;
             if(nums[middle]==target){
                 return middle;
             }
             else if(nums[middle]>target){
                 high=middle;
                 expected=high;
             }
             else{
                 low=middle+1;
                 expected=low;
             }
         }
             
         return expected;
         
     }
}