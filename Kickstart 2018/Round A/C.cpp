#include "../../../stdc++.h"
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
#define loop(i, m, n) for (int i = m; (i) < (n); ++(i))
using namespace std;

inline int char2idx(char c) { return c - 'a'; }

typedef array<int, 26> FREQARY;

FREQARY frequency_array(string str) {
	FREQARY ary;
	repeat(i, 26) { ary[i] = 0; }
	for_each(str.begin(), str.end(), [&](char c){
		ary[char2idx(c)]++;
	});
	return ary;
}

int solve(int L, string W[], char S1, char S2, long N, long A, long B, long C, long D) {
	map<int, map<tuple<char, char>, map<FREQARY, int>>> queries;

	repeat(i, L) {
		int len = W[i].length();
		string substr = W[i].substr(1, len-2);
		tuple<char, char> s_tuple = make_tuple(W[i][0], W[i][len-1]);
		int sublen = substr.length();
		FREQARY freqary = frequency_array(substr);
		if(queries.count(sublen)) {
			if(queries[sublen].count(s_tuple)) {
				if(queries[sublen][s_tuple].count(freqary)) {
					queries[sublen][s_tuple][freqary]++;
				} else {
					queries[sublen][s_tuple][freqary] = 1;
				}
			} else {
				queries[sublen].insert(pair<tuple<char, char>, map<FREQARY, int>> (s_tuple, {{freqary, 1}}));
			}
		} else {
			queries.insert(pair<int, map<tuple<char, char>, map<FREQARY, int>>> (sublen, map<tuple<char, char>, map<FREQARY, int>> ()));
			queries[sublen].insert(pair<tuple<char, char>, map<FREQARY, int>> (s_tuple, {{freqary, 1}}));
		}
	}

	vector<long> temp = {S1, S2};
	loop(i, 2, N) { temp.push_back((A * temp[i-1] + B * temp[i-2] + C) % D); }
	loop(i, 2, N) { temp[i] = 97 + temp[i] % 26; }
	string sentence(temp.begin(), temp.end());

	int count = 0;
	for(auto query_it=queries.begin(); query_it!=queries.end(); query_it++) {
		int sublen = query_it->first;
		FREQARY runnung_freqary = frequency_array(sentence.substr(1, sublen));
		repeat(i, N-sublen-1) {
			for(auto substr_it=query_it->second.begin(); substr_it!=query_it->second.end();) {
				char s1 = get<0>(substr_it->first);
				char s2 = get<1>(substr_it->first);
				if(s1==sentence[i] && s2==sentence[i+sublen+1]) {
					for(auto fa_it=substr_it->second.begin(); fa_it!=substr_it->second.end();) {
						if(runnung_freqary==fa_it->first) {
							count += fa_it->second;
							substr_it->second.erase(fa_it);
							break;
						} else { fa_it++; }
					}
				}
				if(substr_it->second.empty()) {
					query_it->second.erase(substr_it);
					break;
				} else {
					substr_it++;
				}
			}
			if(query_it->second.empty()) {
				break;
			}
			runnung_freqary[char2idx(sentence[i+1])]--;
			runnung_freqary[char2idx(sentence[i+sublen+1])]++;
		}
	}
	return count;
}

int main(void) { _
	int T; cin >> T;
	repeat(t, T) {
		int L; cin >> L;
		string W[L]; repeat(i, L) { cin >> W[i]; }
		char S1, S2; long N, A, B, C, D; cin >> S1 >> S2 >> N >> A >> B >> C >> D;
		int n = solve(L, W, S1, S2, N, A, B, C, D);
		cout << "Case #" << t+1 << ": " << n << endl;
	}
    return 0;
}