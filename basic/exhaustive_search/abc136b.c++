#include<bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    int cnt=0;
    for(int i=1; i<=N; i++){
        if(1<=i and i<=9){
            cnt+=1;
        }
        else if(100<=i and i<=999){
            cnt+=1;
        }
        else if(10000<=i and i<=99999){
            cnt+=1;
        }
    }
    cout << cnt << endl;
}