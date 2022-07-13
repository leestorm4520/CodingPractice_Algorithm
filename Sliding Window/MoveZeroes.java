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
        int[] nums={1,0,1};
        move(nums);
        System.out.println(Arrays.toString(nums));
    }
    public static void move(int[] nums){
        int left=0, right=1;
        while(left<right && right<nums.length){
            int tmp1=nums[left];
            int tmp2=nums[right];
            if(tmp1==0 && tmp2 !=0){
                swap(nums, left, right);
                left++;
                right++;
            }
            if(tmp1!=0) left++;
            if(tmp2==0) right++;
            if(left==right) right++;
            

        }
    }
    public static void swap(int[] nums, int i, int j){
        int tmp=nums[i];
        nums[i]=nums[j];
        nums[j]=tmp;
    }
    
}
