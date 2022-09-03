public class twoPointers {
   static void printKMax(int a[], int n, int k){
    if(k==1){
        for(int i=0;i<n;i++) System.out.println(a[i]+ " ");
        return;
    }
    int p=0, q=k-1, t=p, max=a[k-1];
    while(q<=n-1){
        if(a[p]>max) max=a[p];
        p+=1;
        if(q==p && p!=n){
            System.out.println(max+" ");
            q++;
            p=++t;
            if(q<n) max=a[q];
        }
    }
   }
   public static void main(String[] args){
    int a[]={1,2,3,4,5,6,7,8,9,10};
    int n=a.length;
    int K=3;
    printKMax(a, n, K);
   }
}
