//Stock Span Problem

#include <iostream>
#include<stack>
#include<vector>
#include<utility>
using namespace std;
int main(){
    int data[]={100,80,60,70,60,75,85};
    stack<pair<int,int>> holdData;
    vector<int> returnData;

    //Find the Greater element to the left
    for(int items=0;items<sizeof(data)/sizeof(data[0]);items++){
        if(holdData.size()==0){
            returnData.push_back(items-(-1));
        }else if(holdData.size()>0 && holdData.top().second >= data[items]){
            returnData.push_back(items-holdData.top().first);
        }else if(holdData.size()>0 && holdData.top().second < data[items]){
            while(holdData.size()>0 && holdData.top().second < data[items]){
                holdData.pop();
            }
            if(holdData.size()==0){
                returnData.push_back(items-(-1));
            }else{
                returnData.push_back(items-holdData.top().first);
            }
        }
        holdData.push({items,data[items]});
    }

    for(int data:returnData){
        cout<<data<<" ";
    }
    return 0;
}