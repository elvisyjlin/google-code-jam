#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
using namespace std;

inline bool isOdd(int i) { return i % 2 == 1; }

long solve(string N) {
	repeat(i, N.length()) {
		int digit = N[i] - '0';
		if(isOdd(digit)) {
			string lower = to_string(digit-1) + string(N.length()-i-1, '8');
			if(digit == 9) {
				return stol(N.substr(i))-stol(lower);
			} else {
				string upper = to_string(digit+1) + string(N.length()-i-1, '0');
				return min(stol(upper)-stol(N.substr(i)), stol(N.substr(i))-stol(lower));
			}
		}
	}
	return 0;
}

int main(void) { _
	int T; cin >> T;
	repeat(t, T) {
		cout << "Case #" << t+1 << ": ";
		string N; cin >> N;
		long n = solve(N);
		cout << n << endl;
	}
    return 0;
}