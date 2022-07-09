/*
 * Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
 */


import java.util.*;
public class SquaresOfArray {
    public static void main(String[] args){
        int[] nums={-4,-1,0,3,10};
        int[] result=new int [nums.length];
        for(int i=0;i<result.length;i++){
            result[i]=nums[i]*nums[i];
        }
        quickSort(result, 0, result.length-1);
        for(int num:result) System.out.println(num);

    }

    public static void quickSort(int[] nums, int l, int h){
        if(nums==null || nums.length==0) return;
        if(nums.length==1) return;
        int p;
        if(l<h){
            p=partition(nums, l, h);
            quickSort(nums, l, p-1);
            quickSort(nums, p+1, h);
        }


    }

    public static int partition(int[] nums, int l, int h){
        int i;
        int p;
        int firsthigh;

        p=h;
        firsthigh=l;
        for(i=l;i<h;i++){
            if(nums[i]<nums[p]){
                swap(nums, i, firsthigh);
                firsthigh++;
            }
        }
        swap(nums, p, firsthigh);
        return firsthigh;

    }
    public static void swap(int[] nums, int i1, int i2){
        int tmp=nums[i1];
        nums[i1]=nums[i2];
        nums[i2]=tmp;
    }
}

/*
 * Two pointers solution
 * Create two pointers to track the beginning and the ending of an array
 * 
 * 
 * int n = A.length;
        int[] result = new int[n];
        int i = 0, j = n - 1;
        for (int p = n - 1; p >= 0; p--) {
            if (Math.abs(A[i]) > Math.abs(A[j])) {
                result[p] = A[i] * A[i];
                i++;
            } else {
                result[p] = A[j] * A[j];
                j--;
            }
        }
        return result;

 * 
 */