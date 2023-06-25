#include<bits/stdc++.h>
using namespace std;

int cnt_div(int x){
    int cnt=0;
    while(x){
        if(x%2==0){
            cnt+=1;
        }
        x/=2;
    }
    return cnt;
}
int main(){
    int N;
    cin >> N;
    int mx_cnt=0;
    int ans=0;
    for(int i=1; i<=N; i++){
        if(cnt_div(i)>=mx_cnt){
            mx_cnt=cnt_div(i);
            ans=i;
        }
    }
    cout << ans << endl;
}