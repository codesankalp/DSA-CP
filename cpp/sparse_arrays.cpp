#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
    vector <string> s;
    vector <string> q;
    vector <int> ans;
    int n,m,i=0;
    cin>>n;
    for(i; i<n; i++){
        string temp;
        cin>>temp;
        s.push_back(temp);
    }
    cin>>m;
    for(i=0; i<m; i++){
        string temp;
        cin>>temp;
        q.push_back(temp);
    }
    for(i=0; i<m; i++){
        int a;
        a = count(s.begin(), s.end(), q.at(i));
        ans.push_back(a);
    }
    for(i=0; i<ans.size(); i++){
        cout<<ans.at(i)<<endl;
    }
    return 0;
}