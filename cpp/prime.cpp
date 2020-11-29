#include <iostream>
#include <cmath>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif

	int n;
    bool flag = 1;
	cin >> n;

	for (int i = 2; i <= sqrt(n); i++) {
		if (n % i == 0) {
			cout << "not prime" << endl;
            flag=0;
			break;
		}
	}
	if (flag) {
		cout << "prime" << endl;
	}
	return 0;
}