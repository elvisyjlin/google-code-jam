#include <../../../stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
using namespace std;

double solve(int N, int K, vector<double> V) {
	sort(V.begin(), V.end());
	double sum = 0;
	repeat(i, N) { sum += V[i]; }
	double ek = sum / N;
	repeat(i, K) {
		vector<double>::iterator x = upper_bound(V.begin(), V.end(), ek);
		ek = accumulate(x, V.end(), ek * (x - V.begin())) / N;
	}
	return ek;
}

int main(void) { _
	int T; cin >> T;
	repeat(t, T) {
		int N, K; cin >> N >> K;
		vector<double> V; repeat(i, N) { double v; cin >> v; V.push_back(v); }
		double e = solve(N, K, V);
		printf("Case #%d: %.6f\n", t+1, e);
	}
    return 0;
}