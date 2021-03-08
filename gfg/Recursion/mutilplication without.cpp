#include<iostream>
//Multiplication without using '*' operator using rec
using namespace std;
int mul(int num,int m){
	if (m==0)
	return 0;
	int ans=num+mul(num,m-1);
	return ans;
	
}
int main()
{	
    int num,m;
	cin>>num>>m;
	cout<<"Multiplication without \"*\":"<<mul(num,m);
}
