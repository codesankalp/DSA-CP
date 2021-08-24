/** ONLY ONE LIFE **/
/**    BETRAYED   **/
#include <bits/stdc++.h>
using namespace std;

#define fast                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define ll long long
#define endl "\n"
#define f(a, b, c) for (ll i = a; i < b; i += c)
#define fo(i, a, b, c) for (ll i = a; i < b; i += c)
#define fd(a, b, c) for (ll i = a; i >= b; i -= c)
#define fdo(i, a, b, c) for (ll i = a; i >= b; i -= c)
#define Size(n) ((int)(n).size())
#define all(n) (n).begin(), (n).end()
typedef vector<ll> vl;
typedef vector<vl> vll;
#define pb push_back
#define ff first
#define ss second
#define mp make_pair
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
const int mod = 1e9 + 7;
const int N = (int)2 * 1e5 + 10;
//vector< vector<int>> a(, vector<int> ());

 void solve(){
     ll n ; cin>>n;
     vector<pll> arr(n);
     f(0,n,1){
        ll temp;
        cin>>temp;
        arr[i].first=temp;
        arr[i].second=i;
     }
     if(is_sorted(all(arr))){
         cout<<"YES"<<endl;
         return;
     }else{

         sort(all(arr));
         f(0,n,1){
             if(arr[i].first==arr[i+1].first){
                 if(arr[i].second %2 == arr[i+1].second%2 ){
                     cout<<"NO"<<endl;
                     return;
                 }
                 else{
                     cout<<"YES"<<endl;
                     return;
                 }
    
             }else if((arr[i].second)%2!=0 and (i)%2!=0){
                 continue;
             }else if(arr[i].second%2==0 and (i)%2==0){
                 continue;
             } else{
                 cout<<"NO"<<endl;
                 return;
             }
         }
         cout<<"YES"<<endl;
          














     }
    
}
int main()
{
    fast;

    ll TT;
    // TT=1;
    cin >> TT;

    while (TT--)
    {
     solve();           
    }

    return 0;
}