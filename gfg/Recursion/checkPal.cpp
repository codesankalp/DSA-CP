//check whether the given number is palindrome or not using recursion.
#include<iostream>
using namespace std;
bool checkPal(int arr[],int start,int end){
	if(start>end)
	return true;
    	if(arr[start]==arr[end]){
			return checkPal(arr,start+1,end-1);
		}
		else
			return false;
//output is 1 when given input is palindrome otherwise 0.

		
}
int main(){
	int arr[]={5,4,5};
	cout<<checkPal(arr,0,2);
}
