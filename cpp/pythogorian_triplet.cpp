#include <bits/stdc++.h>
using namespace std;

bool check_pythogorian(int a, int x, int y, int z)
{
    int b, c;
    if (a == x)
    {
        b = y;
        c = z;
    }
    else if (a == y)
    {
        b = x;
        c = z;
    }
    else
    {
        b = y;
        c = x;
    }
    if (a * a == b * b + c * c)
        return true;
    return false;
}

int main()
{
    int x, y, z, a;
    bool ans;
    cin >> x >> y >> z;
    a = max(x, max(y, z));
    ans = check_pythogorian(a, x, y, z);
    if (ans)
        cout << "pythogorian triplet" << endl;
    else
        cout << "not a triplet" << endl;
}