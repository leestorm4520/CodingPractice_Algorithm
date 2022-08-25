#include<iostream>
#include "contactinfo.h"
using namespace std;

int main(){
    ContactInfo entry("John Le","361-742-8909");
    cout << "Name: " <<entry.getName()<<endl;
    cout << "Phone number: "<<entry.getPhoneNumber()<<endl;
    return 0;
}