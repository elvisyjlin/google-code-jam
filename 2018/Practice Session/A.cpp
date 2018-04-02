#include "../../../stdc++.h"                                    // Include all C/C++ standard library
#define _ ios_base::sync_with_stdio(0);cin.tie(0);          // Use all headers
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))      // Define a simple loop
using namespace std;

void solve() {
    int A, B; cin >> A >> B; A++;
    int N; cin >> N;
    while(true) {
        int Q = (A + B) / 2;
        cout << Q << endl;
        string R; cin >> R;
        if(R == "TOO_SMALL") {
            A = Q + 1;
        } else if(R == "TOO_BIG") {
            B = Q - 1;
        } else if(R == "CORRECT") {
            break;
        } else {
            throw R;
        }
    }
}

int main(void) { _
    int T; cin >> T;
    repeat(t, T) {
        solve();
    }
    return 0;
}