#include <bits/stdc++.h>                                    // Include all C/C++ standard library
#define _ ios_base::sync_with_stdio(0);cin.tie(0);          // Use all headers
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))      // Define a simple loop
#define repeat(i, m, n) for (int i = m; (i) < (n); ++(i))   // Define another simple loop
using namespace std;

int solve(int N) {
    return N;
}

int main(void) { _
    int T; cin >> T;
    repeat(t, T) {
        int N; cin >> N;
        int n = solve(N);
        cout << "Case #" << t+1 << ": " << n << endl;
    }
    return 0;
}