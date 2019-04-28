#include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("input4.txt","r",stdin);
    string str;
    while(cin >> str){
        if(str.length()%2){
            cout << "false" << endl;
            continue;
        }
        int i=0;
        string res;
        bool over =false;
        while(i<str.length()){
            if(str[i]!=str[i+1]){
                cout << "false" << endl;
                over=true;
                break;
            }
            res.push_back(str[i]);
            i+=2;
        }
        if(over) continue;
        for(i=0;i<str.length()/2;++i){
            if(str[i]!=str[str.length()-1-i]){
                cout << "false" << endl;
                over=true;
                break;
            }
        }
        if(over) continue;
        cout << res << endl;
    }
    return 0;
}
