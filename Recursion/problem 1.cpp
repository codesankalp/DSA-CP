#include<bits/stdc++.h>
using namespace std;
//Find out the first occurence index of searching element using rec. 
int arrayIndex(int index,int size,int e,int arr[]){
	if(arr[index]==e)
	return index;
	arrayIndex(index+1,size,e,arr);
}
//here 'e' is the element that we search for
int main(){
	int a[5],ele;
	cout<<"enter elements in array:"<<endl;
	for(int i=0;i<5;i++)
	cin>>a[i];
	cout<<"Element which you search for:"<<endl;
	cin>>ele;
	int result=arrayIndex(0,5,ele,a);
	cout<<result<<endl;
	return 0;
}
