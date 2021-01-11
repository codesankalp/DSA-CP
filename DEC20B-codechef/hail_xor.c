#include <stdio.h>
#include <math.h>
typedef long long int ll;
ll min(ll, ll);
int main()
{
    ll test;
    scanf("%lld", &test);
    while (test--)
    {
        ll i, j, p, t, n, x;
        scanf("%lld %lld", &n, &x);
        ll b[100001];
        for (i = 0; i < n; i++)
        {
            scanf("%lld", &b[i]);
        }
        i = 0;
        j = 1;
        ll x2 = x;
        while (i < n - 1 && j < n && x > 0)
        {
            if (b[j] == 0)
            {
                j++;
            }
            if (b[i] != 0)
            {
                if (x <= n)
                {
                    p = log2(min(b[i], b[j]));
                }
                else
                {
                    p = log2(b[i]);
                }
                t = 1 << p;
                b[i] = t ^ b[i];
                b[j] = t ^ b[j];
                x--;
            }
            if (b[i] == 0)
            {
                i++;
                j = i + 1;
            }
        }
        if (b[n - 1] == 0 && b[0] != 0 && x2 >= n)
        {
            i = 0;
            j = n - 1;
            b[j] = b[i];
            b[i] = 0;
        }
        if (n <= 2 && x % 2 != 0)
        {
            i = 0;
            j = 1;
            b[i] = 1 ^ b[i];
            b[j] = 1 ^ b[j];
        }
        for (i = 0; i < n; i++)
        {
            printf("%lld ", b[i]);
        }
        printf("\n");
    }
    return 0;
}
ll min(ll x, ll y)
{
    if (x <= y)
    {
        return x;
    }
    else
    {
        return y;
    }
}