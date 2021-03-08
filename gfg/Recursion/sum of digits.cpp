#include<iostream>
using namespace std;
//Sum of digits of a given number using rec.
int sum(int n){
	 if(n==0)
	 return 0;
	 int digit=n%10;
	 int ans=digit+sum(n/10);
	 return ans;
}
int main()
{	
    int num;
	cin>>num;
	cout<<sum(num);
}
