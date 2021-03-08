#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    deque<int> dq;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    sort(arr, arr + n, greater<int>());
    for (int i = 0; i < n; i++)
    {
        if (!dq.empty())
        {
            dq.push_front(dq.back());
            dq.pop_back();
        }
        dq.push_front(arr[i]);
    }
    deque<int>::iterator it;
    for (it = dq.begin(); it != dq.end(); ++it)
        cout << *it << " ";
    // cout << '\n';

    return 0;
}