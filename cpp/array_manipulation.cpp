#include <bits/stdc++.h>
using namespace std;
bool comp(int a, int b)
{
    return (a < b);
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input1.txt", "r", stdin);
    freopen("output1.txt", "w", stdout);
#endif
    int n, m, max = 0, x = 0, a, b, k;
    vector<int> arr;
    cin >> n >> m;
    for (int i = 0; i <= n + 1; i++) {
        arr.push_back(0);
    }

    for (int i = 0; i < m; i++) {
        cin >> a >> b >> k;
        arr.at(a) += k;
        if ((b + 1) <= n) arr.at(b + 1) -= k;
    }

    for (int i = 1; i <= n; i++) {
        x = x + arr.at(i);
        if (max < x) max = x;
    }

    cout << max;
    return 0;
}