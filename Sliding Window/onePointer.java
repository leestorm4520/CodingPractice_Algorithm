/*
 * Window Sliding Technique is a computational technique to reduce the use of tested loop
 * and replace with single loop, reducing T(N)
 * 
 * size of window is fixed
 */

public class slidingImplement {
    static int maxSum(int arr[], int n, int k){
        if(n<k){
            System.out.println("Invalid");
            return -1;
        }
        int maxSum=0;
        for(int i=0; i<k;i++) maxSum+=arr[i];
        int windowSum= maxSum;
        for(int i=k; i<k;i++){
            windowSum+=arr[i]-arr[i-k];
            maxSum=Math.max(maxSum, windowSum);
        }
        return maxSum;
    }
    public static void main(String[] args){
        int arr[]={1,4,2,10,2,3,1,0,20};
        int k=4;
        int n=arr.length;
        System.out.println(maxSum(arr, n, k));
    }
    
}
