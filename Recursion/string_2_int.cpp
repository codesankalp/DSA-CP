#include<iostream>
#include<math.h>
using namespace std;
//converting str to int using rec
int string_to_int(int l,char str[]){
	if(str[0]=='\0'){
		 return 0;
	}
	int last_digit=str[0];
	int ans=(last_digit-'0')*pow(10,l-1)+string_to_int(l-1,str+1);
	return ans;
}
int length(char str[]){
	if (str[0]=='\0')
	return 0;
    return 1+ length(str+1);	
}
int main()
{
	char str[]="12345";
    int l=length(str);
	cout<<string_to_int(l,str);
	
}
