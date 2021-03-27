//Longest valid paranthesis
#include<typeinfo>
#include<stack>
#include<unordered_map>
using namespace std;

bool balancedBrackets(string str) {
  // Write your code here.
	stack<char> bracket;
	string open="[{(";
	string closing=")}]";
	unordered_map<char,char> matchit{
		{']','['},{'}','{'},{')','('}};
	for(char brack:str){
		if(open.find(brack)!=-1){
			bracket.push(brack);
		}else if(closing.find(brack)!=-1){
			if(bracket.size()==0){
				return false;
			}
			if(bracket.top()==matchit[brack]){
				bracket.pop();
			}else{
				return false;
			}
		}
	}
  return bracket.size()==0;
}