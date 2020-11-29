#include <iostream>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif

	int n, i;

	cin >> n;

	for (i = 2; i < n; i++) {
		if (n % i == 0) {
			cout << "not prime" << endl;
			break;
		}
	}
	if (i == n) {
		cout << "prime" << endl;
	}
	return 0;
}