#include <iostream>
#include <cmath>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif

	int n;
    cin>>n;

    int reverse=0;
    while(n>0){
        int lastDigit = n%10;
        reverse = reverse*10 + lastDigit;
        n = n/10;
    }
    cout<<reverse;
	return 0;
}