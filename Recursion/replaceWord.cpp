#include<iostream>
using namespace std;
//replace a given char in a string using rec
void replaceChar(char word[]){
	if(word[0]=='\0'){
		return;
	}
	if(word[0]=='a'){
			for(int i =0;word[i]!='\0';i++){
					word[i]=word[i+1];
			}
				 replaceChar(word);				
	}
	else
	replaceChar(word+1);	
}
int main(){
	char word[]="abcdabadaf";
	replaceChar(word);
	cout<<word;
}
