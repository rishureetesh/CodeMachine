//Nearest Greater to Right

#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int main(){
    int arr[]={3,1,5,2,8};
    vector<int> returnArray;
    stack<int> holdElements;

    for(int i=sizeof(arr)/sizeof(arr[0])-1;i>=0;i--){
        if(holdElements.size()==0){
            returnArray.push_back(-1);
        }else if(holdElements.size()>0 && holdElements.top()>arr[i]){
            returnArray.push_back(holdElements.top());
        }else if(holdElements.size()>0 && holdElements.top() <= arr[i]){
            while(holdElements.size() > 0 && holdElements.top() <= arr[i]){
                holdElements.pop();
            }
            if(holdElements.size()==0){
                returnArray.push_back(-1);
            }else{
                returnArray.push_back(holdElements.top());
            }
        }
        holdElements.push(arr[i]);
    }
    for(int item=returnArray.size()-1;item>=0;item--)
        cout<<returnArray.at(item)<<endl;
}