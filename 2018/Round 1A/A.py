def solve():
    # Read input
    R, C, H, V = map(int, input().split())
    choco = []
    for _ in range(R):
        choco.append([0] * C)
    choco_row, choco_col = [0]*R, [0]*C
    num_choco = 0
    for i in range(R):
        row = input()
        for j in range(C):
            if row[j] == '@':
                choco_col[j] += 1
                choco[i][j] = 1
        choco_row[i] = row.count('@')
        num_choco += choco_row[i]
    # Find H and V cuts
    if num_choco == 0:
        return 'POSSIBLE'
    H_idx, V_idx = [], []
    flag = True
    if num_choco%(H+1)==0 and num_choco%(V+1)==0:
        num_choco_h = num_choco/(H+1)
        num_choco_v = num_choco/(V+1)
        accum = 0
        for i, r in enumerate(choco_row):
            accum += r
            if accum == num_choco_h:
                accum = 0
                H_idx.append(i)
            elif accum > num_choco_h:
                flag = False
                break
        if not flag:
            return 'IMPOSSIBLE'
        accum = 0
        for i, c in enumerate(choco_col):
            accum += c
            if accum == num_choco_v:
                accum = 0
                V_idx.append(i)
            elif accum > num_choco_v:
                flag = False
                break
        if not flag:
            return 'IMPOSSIBLE'
    else:
        return 'IMPOSSIBLE'
    # Check each piece
    r_from = 0
    num_prev = None
    for r in H_idx:
        c_from = 0
        for c in V_idx:
            num = 0
            for i in range(r_from, r+1):
                for j in range(c_from, c+1):
                    num += choco[i][j]
            if num_prev is None:
                num_prev = num
            elif num_prev != num:
                return 'IMPOSSIBLE'
            c_from = c+1
        r_from = r+1
    return 'POSSIBLE'

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: {}'.format(t+1, solve()))
        