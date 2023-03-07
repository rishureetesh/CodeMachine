//Nearest smallest to Right

#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int main(){
    int arr[]={3,1,5,2,8};
    stack<int> returnArray;
    stack<int> holdElements;

    for(int i=sizeof(arr)/sizeof(arr[0])-1;i>=0;i--){
        if(holdElements.size()==0){
            returnArray.push(-1);
        }else if(holdElements.size()>0 && holdElements.top()<arr[i]){
            returnArray.push(holdElements.top());
        }else if(holdElements.size()>0 && holdElements.top() >= arr[i]){
            while(holdElements.size() > 0 && holdElements.top() >= arr[i]){
                holdElements.pop();
            }
            if(holdElements.size()==0){
                returnArray.push(-1);
            }else{
                returnArray.push(holdElements.top());
            }
        }
        holdElements.push(arr[i]);
    }
    while(returnArray.size()>0){
        cout<<returnArray.top()<<" ";
        returnArray.pop();
    }
}