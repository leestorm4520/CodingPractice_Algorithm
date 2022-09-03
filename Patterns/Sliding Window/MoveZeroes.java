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
        int[] nums={4,2,4,0,0,3,0,5,1,0};
        move1(nums);
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

    public static void move1(int[] nums){
        int[] result=new int[nums.length];
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                result[j]=nums[i];
                j++;
            } 
        }
        Arrays.fill(result, j+1, nums.length-1, 0);
        for(int i=0;i<nums.length;i++) nums[i]=result[i];
    }

    public void move2(int[] nums) {
        int snowBallSize = 0; 
        for (int i=0;i<nums.length;i++){
	        if (nums[i]==0){
                snowBallSize++; 
            }
            else if (snowBallSize > 0) {
	            int t = nums[i];
	            nums[i]=0;
	            nums[i-snowBallSize]=t;
            }
        }
    }
    //fastest
    public void move3(int[] nums){
        int i, j=0;
        for(i=0;i<nums.length;i++){
            if(nums[i]!=0){
                nums[j]=nums[i];
                j++;
            }
        }
        for(i=j;i<nums.length;i++) nums[i]=0;
    }

    public static void swap(int[] nums, int i, int j){
        int tmp=nums[i];
        nums[i]=nums[j];
        nums[j]=tmp;
    }
    
}
