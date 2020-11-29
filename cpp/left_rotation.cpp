#include <iostream>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
    int n,d,i=0;
    cin>>n>>d;
    int arr[n] = {0};
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    d = d%n;
    for(int i=d; i<n; i++){
        cout<<arr[i]<<" ";
    }
    for(int i=0; i<d; i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}