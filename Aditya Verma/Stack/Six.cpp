//Maximum area of histogram

#include<iostream>
#include<stack>
#include<vector>
using namespace std;

int main(){
    int data[]={6,2,5,4,5,1,6};
    stack<pair<int,int>> holdData;
    stack<pair<int,int>> holdDataRight;
    vector<int> areaStorage;

    int length=sizeof(data)/sizeof(data[0]);
    for(int item=0;item<length;item++){
        if(holdData.empty()){
            areaStorage.push_back(item-(-1));
        }else if(holdData.size()>0 && holdData.top().second<data[item]){
            areaStorage.push_back(item-holdData.top().first);
        }else if(holdData.size()>0 && holdData.top().second>=data[item]){
            while(holdData.size()>0 && holdData.top().second>=data[item]){
                holdData.pop();
            }
            if(holdData.empty()){
                areaStorage.push_back(item - (-1));
            }else{
                areaStorage.push_back(item-holdData.top().first);
            }
        }
        holdData.push({item,data[item]});
    }
    for(int item=length-1;item>=0;item--){
        if(holdDataRight.empty()){
            areaStorage[item]+=length-item-1;
        }else if(holdDataRight.size()>0 && holdDataRight.top().second<data[item]){
            areaStorage[item]+=holdDataRight.top().first-item-1;
        }else if(holdDataRight.size()>0 && holdDataRight.top().second>=data[item]){
            while(holdDataRight.size()>0 && holdDataRight.top().second>=data[item]){
                holdDataRight.pop();
            }
            if(holdDataRight.empty()){
                areaStorage[item]+=length-item-1;
            }else{
                areaStorage[item]+=holdDataRight.top().first-item-1;
            }
        }
        holdDataRight.push({item,data[item]});
    }
    int max=0;
    for(int item=0;item<length;item++){
        if(max < areaStorage[item]*data[item]){
            max=areaStorage[item]*data[item];
        }
    }
    cout<<"Max area will be : "<<max;
    return 0;
}