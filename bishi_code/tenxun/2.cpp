#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("input4.txt","r",stdin);
    int n;
    scanf("%d",&n);
    int req[n];
    int res=0;
    for(int i=0;i<n;++i){
        scanf("%d",&req[i]);
    }
    int lastin=0;
    int lastout=0;
    for(int i=0;i<n;++i){
        if(req[i]<0){
            for(int j=lastout;j<i;++j){
                if(req[j]<=0) continue;
                if(req[j]>=-req[i]){
                    req[j]+=req[i];
                    res+=req[i]*(j-i);
                    req[i]=0;
                    break;
                }
                else{
                    res+=req[j]*(i-j);
                    req[i]+=req[j];
                    req[j]=0;
                    lastout=j;
                }
            }
        }
        else if(req[i]>0){
            for(int j=lastin;j<i;++j){
                if(req[j]>=0) continue;
                if(req[i]+req[j]>0){
                    req[i]+=req[j];
                    res+=req[j]*(j-i);
                    req[j]=0;
                    lastin=j;
                }
                else{
                    req[j]+=req[i];
                    res+=req[i]*(i-j);
                    req[i]=0;
                    break;
                }
            }
        }
    }
    printf("%d\n",res);
    return 0;
}
