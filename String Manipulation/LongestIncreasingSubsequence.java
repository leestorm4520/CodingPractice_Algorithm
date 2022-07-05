package String Manipulation;

public class LongestIncreasingSubsequence {
    public static void main(String[] args){
        int[] arr={5,2,8,6,3,6,9,5};
        System.out.println(maxIncreasing(arr));
    }

    public static int maxIncreasing(int[] arr){
        if(arr==null || arr.length==0) return 0;
        if(arr.length==1) return 1;
        
        int[] result=new int[arr.length];
        int maxIncreasing=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i-1]<arr[i]){
                maxIncreasing=1+Math.max(maxIncreasing, maxIncreasing[0-> (i-1)]);
            }
        }
    }
}
