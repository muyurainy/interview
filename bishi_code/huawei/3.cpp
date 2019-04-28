#include<stdio.h>
#include <map>
#include <cstring>
using namespace std;

char s[100000];
int a[15];
int z[40];
void Remove(char n[],int cnt){
    for(int i=0;i<strlen(n);i++)
        z[n[i]-'a']-=cnt;
}
int main(){
    gets(s);
    for(int i=0;i<strlen(s);i++){
        if(s[i]>='A'&&s[i]<='Z')
            s[i]='a'+s[i]-'A';
        z[s[i]-'a']++;
    }
    a[6]=z['x'-'a'];
    Remove("six",a[6]);
    a[0]=z['z'-'a'];
    Remove("zero",a[0]);
    a[4]=z['u'-'a'];
    Remove("four",a[4]);
    a[5]=z['f'-'a'];
    Remove("five",a[5]);
    a[3]=z['r'-'a'];
    Remove("three",a[3]);
    a[8]=z['g'-'a'];
    Remove("eight",a[8]);
    a[2]=z['t'-'a'];
    Remove("two",a[2]);
    a[9]=z['i'-'a'];
    Remove("nine",a[9]);
    a[7]=z['s'-'a'];
    Remove("seven",a[7]);
    a[1]=z['o'-'a'];
    for(int i=0;i<10;i++){
        while(a[i]--)
            printf("%d",i);
    }
    printf("\n");
    return 0;
}
/*
oNEthreefoursixninenien
*/