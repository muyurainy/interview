#include<stdio.h>
#include <map>
#include <cstring>
using namespace std;

#define INF 0x3fffffff
int a[200][200];
int dis[200];
bool vis[200];
int N,M;
int s,t,v;
void Dij(){
    memset(vis,0,sizeof(vis));
    for(int i=1;i<=N;i++)
        dis[i]=INF;
    dis[s]=0;
    for(int i=1;i<=N;i++){
        int Min=INF,pos;
        for(int j=1;j<=N;j++){
            if(Min>dis[j]&&!vis[j]){
                pos=j;
                Min=dis[j];
            }
        }
        if(Min==INF)
            break;
        vis[pos]=1;
        for(int j=1;j<=N;j++){
            if(a[pos][j]!=-1){
                if(pos==s)
                    dis[j]=min(dis[j],dis[pos]+a[pos][j]);
                else
                    dis[j]=min(dis[j],dis[pos]+a[pos][j]-1);
            }
        }
    }
}
int main(){
    memset(a,-1,sizeof(a));
    scanf("%d%d",&N,&M);
    int lu;
    for(int i=0;i<M;i++){
        scanf("%d%d%d%d",&lu,&s,&t,&v);
        a[s][t]=a[t][s]=v;
    }
    scanf("%d%d",&s,&t);
    Dij();
    if(dis[t]==-1)
        printf("NO");
    else
        printf("%d\n",dis[t]);
    return 0;
}
/*
4 5
1 1 2 3
2 1 3 3
3 1 4 4
4 2 3 5
5 3 4 3
1 3
*/