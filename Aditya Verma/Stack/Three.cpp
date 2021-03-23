//Nearest smallest to Left

#include <iostream>
#include<vector>
#include<stack>
using namespace std;
int main(){
    int arr[]={3,1,5,2,8};
    vector<int> holdResult;
    stack<int> manipulateData;

    for(int item:arr){
        if(manipulateData.size()==0){
            holdResult.push_back(-1);
        }else if(manipulateData.size()>0 && manipulateData.top() < item){
            holdResult.push_back(manipulateData.top());
        }else if(manipulateData.size()>0 && manipulateData.top() > item){
            while(manipulateData.size()>0 && manipulateData.top() > item){
                manipulateData.pop();
            }
            if(manipulateData.size()==0){
                holdResult.push_back(-1);
            }else{
                holdResult.push_back(manipulateData.top());
            }
        }
        manipulateData.push(item);
    }
    for(int item:holdResult)
        cout<<item<<" ";
}