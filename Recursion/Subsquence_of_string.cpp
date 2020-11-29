#include<iostream.h>
using namespace std;
//Getting subsequences of string using rec
void str_subs(string input,string output){
	if(input.length()==0){
		cout<<output<<endl;
		return;
	}
		str_subs(input.substr(1),output+input[0]);
		str_subs(input.substr(1),output);
	
}
int main (){
	string input;
	string output="";
	cin>>input;
	str_subs(input,output);
}
