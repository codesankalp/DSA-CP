#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, n2, q, t, one_cnt = 0;
    cin >> n >> n2;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        one_cnt++;
    }
    while (n2--)
    {
        cin >> t >> q;
        if (t == 1)
        {
            if (a[q - 1] == 1)
                one_cnt--;
            else
                one_cnt++;
            a[q - 1] = 1 - a[q - 1];
        }
        else if (t == 2)
        {
            if (q <= one_cnt)
                cout << "1" << endl;
            else
                cout << "0" << endl;
        }
    }
}