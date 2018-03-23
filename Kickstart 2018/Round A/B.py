# E[0] = sum(Vi/N)
# E[k] = sum(max(Vi, E[k-1])/N)

def expectation(N, K, V, mean):
    # # Recursion form fails
    # if K == 0: return mean
    # e = expectation(N, K-1, V, mean)
    # return sum(max(v, e)/N for v in V)

    ek = mean
    for k in range(K):
        ek = sum(max(v, ek)/N for v in V)
    return ek

def solve(N, K, V):
    mean = sum(V) / N
    # return expectation(N, K, V, mean)
    return expectation_faster(N, K, sorted(V), mean)

def expectation_faster(N, K, V, mean):
    # # Recursion form fails
    # if K == 0: return mean
    # e = expectation_faster(N, K-1, V, mean)
    # x = binary_search(V, e)
    # if isinstance(x, tuple): x = x[1]
    # return e * x / N + sum(v for v in V[x:]) / N

    ek = mean
    for k in range(K):
        x = binary_search(V, ek)
        if isinstance(x, tuple): x = x[1]
        ek = ek * x / N + sum(v for v in V[x:]) / N
    return ek

def binary_search(array, value):
    lo, hi, mid = 0, len(array), 0
    while lo < hi:
        mid = (lo + hi) // 2
        if value < array[mid]:
            hi = mid
        elif value > array[mid]:
            lo = mid + 1
        else:
            return mid
    lo = mid if value > array[mid] else mid - 1
    hi = mid if value < array[mid] else mid + 1
    return (lo, hi)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N, K = map(int, input().split())
        V = list(map(int, input().split()))
        e = solve(N, K, V)
        print('Case #{}: {:.6f}'.format(t, e))