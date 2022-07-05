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
        result[0]=1;

        for(int i=1;i<arr.length;i++){
            if(arr[i-1]<arr[i]){
                result[i]=1 + findMaxLength(result, i-1);
            }
        }
        return result[result.length-1];
    }
    public static int findMaxLength(int[] result, int index){
        int maxLength=0;
        for(int i=0;i<index;i++)
            if(maxLength<=result[i]) maxLength=result[i];
        return maxLength;
    }
}
