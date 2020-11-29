#include<bits/stdc++.h>
using namespace std;
//Find out the last occurence index of searching element using rec. 
int arrayIndex(int size,int e,int arr[]){
	if(size!=-1){
		if(arr[size]==e)
		return size;
		arrayIndex(size-1,e,arr);
	}
	else
	return -1;
	
}
int main(){
	int a[5],ele;
	cout<<"Enter elements in array:"<<endl;
	for(int i=0;i<5;i++)
	cin>>a[i];
	cout<<"Element which you search for:"<<endl;
	cin>>ele;
	int result=arrayIndex(4,ele,a);
	cout<<result<<endl;
	return 0;
}
