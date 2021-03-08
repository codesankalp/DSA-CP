#include<iostream>
using namespace std;
//Raising a number to its power without using in-built function 
//using recursion
int pow(int x,int n){
 	if (n==1){
 		return x;
	 }
	 int ans=x*pow(x,n-1);
	 return ans;
 }
int main() 
{	
	int number,power;
	cout<<"Enter the number and its power"<<endl;
	cin>>number>>power;
	cout<<"Result:"<<pow(number,power);
	return 0;
}
