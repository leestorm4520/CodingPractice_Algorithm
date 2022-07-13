/*
 * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 */
import java.util.*;
public class MoveZeroes {
    public static void main(String[] args){
        int[] nums={0,1,0,3,12};
        move(nums);
        System.out.println(Arrays.toString(nums));
    }
    public static void move(int[] nums){
        int i=0;
        int left=0, right=nums.length-1;
        while(left<right){
            int temp=nums[i];
            if(temp==0 && nums[right]!=0){
                swap(nums, i, right);
                right--;
            }
            if(temp==0 && nums[left]!=0){
                swap(nums, i, left);
                left++;
            }
        }
    }
    public static void swap(int[] nums, int i, int j){
        int tmp=nums[i];
        nums[i]=nums[j];
        nums[j]=tmp;
    }
    
}
