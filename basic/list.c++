#include<bits/stdc++.h>
using namespace std;

int main(){
    int q;
    cin >> q;
    list<int> L;
    auto itr = L.end(); //イテレーターitrをLの末尾とする
    for(int i=0; i<q; i++){
        int type;
        cin >> type;

        if(type==0){
            int x;
            cin >> x;
            L.insert(itr, x); //現在のイテレータitrの位置にxを挿入
            itr--; //イテレータitrを1つ前に動かす
        }
        else if(type==1){
            int d;
            cin >> d;
            for(int j=0; j<d; j++){
                itr++; //イテレータitrを1つ後方に動かす
            }
            for(int j=0; j<-d; j++){
                itr--; //イテレータitrを1つ前方に動かす
            }
        }
        else{
            auto itrc = itr; //イテレータitrをコピーしてitrcとする
            itrc++; //コピーしたイテレータitrcを1つ後方に動かす
            L.erase(itr); //イテレータitrの指す要素を消す
            itr = itrc; //コピーしておいたイテレータitrcをitrに戻す
        }
    }
    itr = L.begin(); //イテレータitrを先頭とする
    while(itr!=L.end()){ //イテレータitrが末尾に着くまで繰り返す
        cout << *itr << endl; //イテレータitrの指す要素を出力する
        itr++; //イテレータを後方に動かす
    }
    return 0;
}