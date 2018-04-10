import math

def solve():
    table = {}

    D, P = input().split()
    D = int(D)

    d = 1
    damage = 0
    num_shoot = 0
    max_shoot_damage = 0
    for p in P:
        if p == 'S':
            if d in table:
                table[d] += 1
            else:
                table[d] = 1

            damage += d
            num_shoot += 1
            max_shoot_damage = d
        else: # p == 'C'
            d *= 2

    if num_shoot == 0:
        num_hack = 0
    elif D < num_shoot:
        num_hack = 'IMPOSSIBLE'
    elif D == num_shoot:
        num_hack = 0
        for k, v in table.items():
            num_hack += int(math.log2(k)) * v
    else:
        num_hack = 0
        current_damage = max_shoot_damage
        while damage > D:
            total_reduce = current_damage / 2 * table[current_damage]
            if damage - D <= total_reduce:
                num_hack += math.ceil((damage - D) / (current_damage / 2))
                break
            else:
                damage -= total_reduce
                num_hack += table[current_damage]
                table[current_damage/2] += table[current_damage]
                current_damage /= 2
    return num_hack

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        res = solve()
        print('Case #{}: {}'.format(t+1, res))