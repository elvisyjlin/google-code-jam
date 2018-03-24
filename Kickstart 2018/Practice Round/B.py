import math

def solve():
    i = int(input())
    s = 0
    while i != 1:
        l = math.log2(i)
        if l.is_integer():
            return s
        i = (1 << math.ceil(l)) - i
        s = 1 - s
    return s

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        s = solve()
        print('Case #{}: {}'.format(t+1, s))