def solve():
    S = int(input())
    D, A, B = [], [], []
    for i in range(S):
        d, a, b = map(int, input().split())
        D.append(d)
        A.append(a)
        B.append(b)

    temp = [] # [start, m, n]
    lengths = {} # [len: set([starts])]

    for i in range(S):
        to_remove = []
        for t in temp:
            if t[1] == None or t[2] == None:
                if t[1] != D[i] + A[i] and t[2] == None:
                    t[2] = D[i] - B[i]
                elif t[1] == None and t[2] != D[i] - B[i]:
                    t[1] = D[i] + A[i]
            elif t[1] != D[i] + A[i] and t[2] != D[i] - B[i]:
                length = i - t[0]
                if length in lengths:
                    lengths[length].add(t[0])
                else:
                    lengths[length] = set([t[0]])
                to_remove.append(t)
        for r in to_remove:
            temp.remove(r)
        temp.append([i, D[i] + A[i], None])
        temp.append([i, None, D[i] - B[i]])
    
    for t in temp:
        length = S - t[0]
        if length in lengths:
            lengths[length].add(t[0])
        else:
            lengths[length] = set([t[0]])

    largest = max(lengths.keys())
    print('{} {}'.format(largest, len(lengths[largest])))

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: '.format(t+1), end='')
        solve()