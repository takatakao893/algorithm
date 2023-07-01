#include<bits/stdc++.h>
using namespace std;

int main(){
    int q;
    cin >> q;
    deque<int> A;
    for(int i=0; i<q; i++){
        int type;
        cin >> type;
        if(type==0){
            int d,x;
            cin >> d >> x;
            if(d==0){
                A.push_front(x);
            }
            else if(d==1){
                A.push_back(x);
            }
        }
        else if(type==1){
            int p;
            cin >> p;
            cout << A[p] << endl;
        }
        else{
            int d;
            cin >> d;
            if(d==0){
                A.pop_front();
            }
            else if(d==1){
                A.pop_back();
            }
        }
    }

}
