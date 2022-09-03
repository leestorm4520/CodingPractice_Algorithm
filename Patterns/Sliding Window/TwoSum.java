/*
 * Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.package Sliding Window;


 */
import java.util.*;
public class TwoSum {

    public static void main(String[] args){
        int[] nums= {2,7,11,15};
        int target=9;
        System.out.println(Arrays.toString(twoSum(nums, target)));

    }
    public static int[] twoSum(int[] nums, int target){
        int[] result={0,0};
        int i=0;
        HashMap<Integer,Integer> numHash=new HashMap<>();
        for(i=0;i<nums.length;i++) numHash.put(nums[i],i);
        i=0;
        while(result[0]==0 && i<nums.length){
            int tmp=target -nums[i];
            if(numHash.containsKey(tmp)){
                result[0]=Math.min(i,numHash.get(tmp));
                result[1]=Math.max(i,numHash.get(tmp));
            }
            i++;
        }
        return result;
    }
}