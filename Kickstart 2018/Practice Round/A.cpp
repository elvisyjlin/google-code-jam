#include "../../../stdc++.h"
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
using namespace std;

void solve() {
    int N; cin >> N;
    int a[N], b[N]; repeat(i, N) { cin >> a[i] >> b[i]; }
    int P; cin >> P;
    repeat(i, P) {
        int p; cin >> p;
        int count = 0;
        repeat(j, N) {
            if(a[j]<=p && b[j]>=p) {
                count++;
            }
        }
        cout << " " << count;
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