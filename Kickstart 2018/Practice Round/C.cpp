#include "../../../stdc++.h"
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
using namespace std;

void solve() {
    int N; cin >> N;
    map<string, string> trip;
    set<string> srcs;
    set<string> dsts;
    repeat(i, N) {
        string src, dst; cin >> src >> dst;
        trip.insert(pair<string, string> (src, dst));
        srcs.insert(src);
        dsts.insert(dst);
    }
    string start;
    for(auto src : srcs) {
        if(!dsts.count(src)) {
            start = src;
            break;
        }
    }
    while(trip.count(start)) {
        cout << " " << start << "-" << trip[start];
        start = trip[start];
    }
    cout << endl;
}

int main(void) { _
    int T; cin >> T;
    repeat(t, T) {
        cout << "Case #" << t+1 << ":";
        solve();
    }
    return 0;
}