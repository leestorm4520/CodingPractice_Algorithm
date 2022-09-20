using namespace std;
#include<iostream>
#include<vector>
#include<algorithm>

class SlidingWindow{

    public:
    static vector<double> findAverage(int K, const vector<int> &arr){
        vector<double> result(arr.size()-K+1);
        double windowSum=0.0;
        int windowStart=0;
        for(int windowEnd=0;windowEnd<arr.size();windowEnd++){
        windowSum+=arr[windowEnd];
        if(windowEnd>=K-1){
            result[windowStart]=windowSum/K;
            windowSum-=arr[windowStart];
            windowStart+=1;
        }
        }
        return result;

    }
    static double findMax(int K, const vector<int> &arr){
        double windowSum=0;
        double maxAvg=0.0;
        int windowStart=0;
        for(int windowEnd=0;windowEnd<arr.size();windowEnd++){
        windowSum+=arr[windowEnd];
        if(windowEnd>=K-1){
            maxAvg=std::max(maxAvg, windowSum/K);
            windowSum-=arr[windowStart];
            windowStart+=1;
        }
        }
        return maxAvg;

    }

};
int main(int argc, char* argv[]){
  vector<double> avg=SlidingWindow::findAverage(4, vector<int>{3,45,-5,7,26,63,1,67});
  cout<<"Average of subarrays of size 4 is:  ";
  for(double d: avg){
    cout<<d<<" ";
    }
  cout<<endl;
  vector<double> max= AverageOf
}