#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, n, x;
    cin >> t;
    while (t--)
    {
        // cout << t;
        cin >> n >> x;
        int a[n], i = 1, j = 2, q = 0, p, k, c, x2;
        for (q = 0; q < n; q++)
        {
            cin >> a[q];
        }
        x2 = x;
        // if (n > 2)
        // {
        while (x > 0 && i <= n - 1)
        {
            if (a[i - 1] == 0)
                p = 0;
            else
                p = log2(a[i - 1]);
            k = 1 << p;
            a[i - 1] = a[i - 1] ^ k;
            // cout << p << " " << k;
            for (j = i + 1; j <= n; j++)
            {
                c = a[j - 1] ^ k;
                // cout << c << endl;
                if (c < a[j - 1])
                {
                    a[j - 1] = c;
                    break;
                }
            }
            // cout << "-->" << c << endl;
            if (j == n)
                a[n - 1] = c;
            while (a[i - 1] == 0 && a[i - 1] <= n - 1)
            {
                i += 1;
            }
            x--;
            // for (q = 0; q < n; q++)
            // {
            //     cout << a[q] << " ";
            // }
            // cout << endl;
        }
        // }
        // else
        // {
        //     for (q = 0; q < x; q++)
        //     {
        //         if (a[i - 1] == 0)
        //             k = 1;
        //         else
        //         {
        //             p = log2(a[i - 1]);
        //             k = pow(2, p);
        //         }
        //         a[i - 1] = a[i - 1] ^ k;
        //         if (n == 2)
        //             a[j - 1] = a[j - 1] ^ k;
        //     }
        // }
        // while (x > 0 && i <= n - 1)
        // {
        //     if (a[i - 1] == 0)
        //         p = 0;
        //     else
        //         p = log2(a[i - 1]);
        //     k = 1 << p;
        //     a[i - 1] = a[i - 1] ^ k;
        //     for (j = i + 1; j++; j < n + 1)
        //     {
        //         c = a[j - 1] ^ k;
        //         if (c < a[j - 1])
        //         {
        //             a[j - 1] = c;
        //             break;
        //         }
        //     }
        //     if (j == n)
        //         a[j - 1] = c;

        //     while (a[i - 1] == 0 && a[i - 1] <= n - 1)
        //     {
        //         i++;
        //     }
        //     x--;
        // }
        if (a[n - 1] == 0 && a[0] != 0 && x2 > n)
        {
            i = 0;
            j = n - 1;
            a[j] = a[i];
            a[i] = 0;
        }
        if (n <= 2 && x % 2 != 0)
        {
            i = 0;
            j = 1;
            a[i] = 1 ^ a[i];
            a[j] = 1 ^ a[j];
        }

        for (q = 0; q < n; q++)
        {
            cout << a[q] << " ";
        }
        cout << endl;
    }
    return 0;
}