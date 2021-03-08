//To count number of zeros in a given number using rec.
#include<iostream>
using namespace std;
int count_zero(int n){
	if(n==0)
	return 0;
	int smallans=count_zero(n/10);
	int lastdigit=n%10;
	if(lastdigit==0)
	return 1+smallans;
	return smallans;
}
	
int main()
{	
    int num;
	cin>>num;
	cout<<count_zero(num);
}
