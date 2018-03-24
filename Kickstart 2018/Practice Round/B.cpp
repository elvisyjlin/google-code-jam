#include "../../../stdc++.h"
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
using namespace std;

void solve() {
    long K; cin >> K;
    int c = 0;
    while(K != 1) {
        double K_log2 = log2(K);
        if(round(K_log2) == K_log2) {
            break;
        }
        K = (1l << (long)ceil(K_log2)) - K;
        c = 1 - c;
    }
    cout << c << endl;
}

int main(void) { _
    int T; cin >> T;
    repeat(t, T) {
        cout << "Case #" << t+1 << ": ";
        solve();
    }
    return 0;
}