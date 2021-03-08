#include<iostream>
using namespace std;
//Remove duplicates in a string using rec.
void removeDup(char word[]){
	if(word[0]=='\0')
	return;
	if(word[0]==word[1]){
			for(int i=0;word[i]!='\0';i++){
					word[i]=word[i+1];
			}
			removeDup(word);	
	}
	else
		removeDup(word+1);	
}
int main(){
	char word[]="aabbbdcc";
	removeDup(word);
	cout<<word;
}
