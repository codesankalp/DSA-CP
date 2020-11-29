#include <iostream>
#include <cmath>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif

	int n;
	cin >> n;
    int original_n = n;
	int sum=0;
    while(n>0){
        int last_digit = n%10;
        sum += pow(last_digit, 3);
        n = n/10;
    }

    if(sum==original_n) cout<<"armstrong";
    else cout<<"not armstrong";
	return 0;
}