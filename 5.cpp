#include <bits/stdc++.h>
using namespace std;

int main(){
	//freopen("input5.txt","r",stdin);
	int n;
	scanf("%d",&n);
	bool visited[n+1];
	memset(visited,0,sizeof(bool)*(n+1));
	vector<vector<int>> vvi(n+1);
	int a,b;
	for(int i=0;i<n-1;++i){
		scanf("%d%d",&a,&b);
		vvi[a].push_back(b);
		vvi[b].push_back(a);
	}
	int res=0;
	visited[1]=true;
	for(const auto &entry:vvi[1]){
		int sum=1;
		visited[entry]=true;
		queue<int> q;
		q.push(entry);
		while(!q.empty()){
			bool exist=false;
			for(const auto &node:vvi[q.front()]){
				if(visited[node]) continue;
				exist=true;
				++sum;
				visited[node]=true;
				q.push(node);
			}
			if(!exist) break;
			q.pop();
		}
		res=max(res,sum);
	}
	printf("%d\n",res);
	return 0;
}
