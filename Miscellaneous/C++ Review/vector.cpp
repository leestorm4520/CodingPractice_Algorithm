#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int>v;

    for(int i=0;i<5;i++) v.push_back(i);
    cout<<"Output: ";
    for(auto i=v.begin();i!=v.end();i++) cout<<*i<<" ";
    cout<<endl;
    for(auto i=v.cbegin();i!=v.cend();i++) cout<<*i<<" ";
    cout << "\nOutput of rbegin and rend: ";
    for (auto ir = v.rbegin(); ir != v.rend(); ++ir)
        cout << *ir << " ";
 
    cout << "\nOutput of crbegin and crend : ";
    for (auto ir = v.crbegin(); ir != v.crend(); ++ir)
        cout << *ir << " ";

    return 0;
}