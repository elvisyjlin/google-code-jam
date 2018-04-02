#include "../../../stdc++.h"
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define LLI long long int
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
#define loop(i, m, n) for (int i = m; (i) < (n); ++(i))
using namespace std;

#define MAX_N   200002
#define MAX_VAL 100
int N, Q;
int ary[MAX_N];
int pref[MAX_N];

inline int get_sum(int l, int r) { return pref[r] - pref[l-1]; }

LLI get_sum_at(LLI idx, int n) {
    int lower = 0;
    int upper = MAX_N * MAX_VAL;
    LLI ans = 0;
    while(lower <= upper) {
        int max_val = (lower + upper) / 2;
        int l = 1;
        int r = 1;
        LLI cnt = 0;
        LLI add = ary[1];
        LLI total = 0;
        while(r <= n) {
            if(l > r || get_sum(l, r) < max_val) {
                cnt += r - l + 1;
                total += add;
                r++;
                add += (r - l + 1) * ary[r];
            } else {
                add -= get_sum(l, r);
                l++;
            }
        }
        if(cnt > idx) {
            upper = max_val - 1;
        } else {
            lower = max_val + 1;
            ans = total + (idx-cnt) * max_val;
        }
    }
    return ans;
}

void solve() {
    ary[0] = pref[0] = 0;

    cin >> N >> Q;
    loop(i, 1, N+1) { cin >> ary[i]; }
    loop(i, 1, N+1) { pref[i] = pref[i-1] + ary[i]; }

    repeat(i, Q) {
        LLI l, r; cin >> l >> r;
        cout << get_sum_at(r, N) - get_sum_at(l-1, N) << endl;
    }
}

int main(void) { _
    int T; cin >> T;
    repeat(t, T) {
        cout << "Case #" << t+1 << ":" << endl;
        solve();
    }
    return 0;
}