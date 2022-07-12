/*
 * Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 */
import java.util.*;
public class RotateArray {
    public static void main(String[] args){
        int[] nums= {-1,-100,3,99};
        int k=2;
        rotate(nums, k);
        System.out.println(Arrays.toString(nums));

    }   
    //M1: work but took too long
    // public static void rotate (int[] nums, int k){
    //    ArrayList<Integer> result=new ArrayList<Integer>(nums.length);
    //    for(int num: nums) result.add(num);
    //    for(int i=0;i<k;i++){
    //         int temp=result.get(result.size()-1);
    //         result.remove(result.size()-1);
    //         result.add(0,temp);
    //    }
    //    for(int i=0;i<nums.length;i++) nums[i]=result.get(i);
    // }
    public static void rotate (int[] nums, int k){
        k=k%nums.length;
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums.length-1);
    }
    public static void swap(int[] nums, int i, int j){
        int temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
    }
    public static void reverse(int[] nums, int left, int right){
        while(left<right){
            swap(nums, left, right);
            left++;
            right--;
        }
    }
}