//Recursion for adding digits of a number
#include <iostream>
using namespace std;
class SumDigits {
    public:
    int addDigits(int number){
        return number/10 == 0 ? number%10 : number % 10 + addDigits(number/10);
    }
};
int main() {
    SumDigits sum;
    cout<<sum.addDigits(123)<<endl;
    return 0;
}