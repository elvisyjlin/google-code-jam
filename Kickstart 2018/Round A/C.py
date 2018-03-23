def char2idx(c):
    return ord(c) - ord('a')

def frequency_array(string):
    array = [0] * 26
    for c in string:
        array[char2idx(c)] += 1
    return array

def solve(W, S1, S2, N, A, B, C, D):
    queries = {}
    for w in W:
        end = (w[0], w[-1])
        sub = w[1:-1]
        if len(sub) not in queries:
            queries[len(sub)] = [(end, frequency_array(sub))]
        else:
            queries[len(sub)].append((end, frequency_array(sub)))

    sentence = [S1, S2]
    for i in range(2, N):
        x = (A * sentence[i-1] + B * sentence[i-2] + C) % D
        sentence.append(x)
    for i in range(2, N):
        sentence[i] = 97 + sentence[i] % 26
    sentence = ''.join(map(chr, sentence))

    count = 0
    for l, q in queries.items():
        runnung_freqary = frequency_array(sentence[1:1+l])
        found = set()
        for i in range(len(sentence)-1-l):
            for idx, (s, freqary) in enumerate(q):
                if idx not in found and sentence[i]==s[0] and sentence[i+l+1]==s[1] and runnung_freqary==freqary:
                    count += 1
                    found.add(idx)
            runnung_freqary[char2idx(sentence[i+1])] -= 1
            runnung_freqary[char2idx(sentence[i+l+1])] += 1

    return count

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        L = int(input())
        W = input().split()
        S1, S2, N, A, B, C, D = input().split()
        S1, S2 = list(map(ord, [S1, S2]))
        N, A, B, C, D = list(map(int, [N, A, B, C, D]))
        n = solve(W, S1, S2, N, A, B, C, D)
        print('Case #{}: {}'.format(t, n))