#include <bits/stdc++.h>
using namespace std;

void reverse_ls(int v[], int start, int end)
{
    int temp;
    while (start < end)
    {
        temp = v[start];
        v[start] = v[end];
        v[end] = temp;
        start += 1;
        end -= 1;
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input1.txt", "r", stdin);
    freopen("output1.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    while (t--)
    {
        int n, k, a;
        cin >> n;
        int v[n];
        cin >> k;
        for (int i = 0; i < n; i++)
        {
            cin >> a;
            v[i] = a;
        }
        reverse_ls(v, 0, n - 1);
        reverse_ls(v, 0, k - 1);
        reverse_ls(v, k, n - 1);
        for (int i = 0; i < n; i++)
        {
            cout << v[i] << " ";
        }
    }

    return 0;
}