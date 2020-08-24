#include<iostream>
using namespace std;
// Print 'n'th natural number in desc order using rec.
int print(int n)
{ 
   		if(n==0)
		return 0;
	    cout<<n<<endl;
	    print(n-1);	 
}
int main(){
	int n;
	cin>>n;
	print(n);
}
