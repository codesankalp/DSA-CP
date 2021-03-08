#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

void solve(char arr[], int n)
{
    stack<int> s;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 'X')
        {
            cout << s.top() << endl;
            s.pop();
        }
        else if (arr[i] == 'Y')
        {
            cout << 2 * (s.top()) << endl;
            s.push(2 * (s.top()));
        }
        else if (arr[i] == '+')
        {
            int temp = s.top();
            s.pop();
            int temp2 = s.top();
            cout << temp << temp2 << endl;
            s.push(temp);
            s.push(temp2 + temp);
        }
        else
        {
            cout << "else" << arr[i] << ((int)arr[i] - 48) << endl;
            s.push(((int)arr[i] - '0'));
        }
    }
    int sum = 0;
    while (!s.empty())
    {
        cout << s.top() << " ";
        sum += s.top();
        s.pop();
    }
    cout << sum << endl;
}

int main()
{
    int n, temp;
    cin >> n;
    char arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i];
    }
    // solve(arr, n);
    return 0;
}