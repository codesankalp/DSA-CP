#include <bits/stdc++.h>
using namespace std;

void reverseStr(string &str)
{
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        string start = s.substr(0, 1);
        string prev_min = start + start;
        for (int i = 1; i < n; i++)
        {
            string r = s.substr(0, i);
            string k = s.substr(0, i);
            reverse(r.begin(), r.end());
            prev_min = prev_min < k + r ? prev_min : k + r;
            // cout<<prev_min<<endl;
        }
        cout << prev_min << endl;
    }
    return 0;
}