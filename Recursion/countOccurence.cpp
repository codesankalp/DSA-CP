#include<iostream>
//Count the number of occurence of given number in a using recursion.
//the var count is ppassed by reference to reflect changes in original value 
using namespace std;
void countOccurence(int arr[],int i,int n,int x,int &count){
	if(i==n)
	return;
	if(arr[i]==x)
	count+=1;
    countOccurence(arr,i+1,n,x,count);
}
//here n is lenght of a array and 'x' is the element that we search for. 
int main(){
	int count=0;
	int arr[]={2,4,5,7,5,5,6};
	countOccurence(arr,0,7,5,count);
	cout<<count;
}
