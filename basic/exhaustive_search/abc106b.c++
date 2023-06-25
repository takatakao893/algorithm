#include<bits/stdc++.h>
using namespace std;

int cnt_divisor(int n){
    int divi=0;
    for(int i=1; i<=n; i++){
        if(n%i==0){
            divi+=1;
        }
    }
    return divi;
}
int main(){
    int N;
    cin >> N;
    int cnt=0;
    for(int i=1; i<=N; i++){
        if(i%2==1 and cnt_divisor(i)==8){
            cnt+=1;
        }
    }
    cout << cnt << endl;
}