"""No.84 candidate: fully reproducible finite existence certificate.
No external packages. Python >=3.8.
Bit position 0 is the first (leftmost) coordinate in the displayed column order.
"""
from itertools import combinations

COLS = [2, 8, 1, 10, 12, 13, 14, 15, 4, 3, 6, 5, 7, 9, 11]
SYNDROME = 4
N = len(COLS)
FORBIDDEN_RUN = 11
WITNESSES = [13, 13, 4, 4, 4]


def syndrome(mask):
    ans = 0
    for i, col in enumerate(COLS):
        if mask & (1 << i):
            ans ^= col
    return ans


def dot(a, b):
    return (a & b).bit_count() & 1


def contains_run(mask, length):
    chunk = (1 << length) - 1
    return any(((mask >> start) & chunk) == chunk
               for start in range(N - length + 1))


def main():
    assert sorted(COLS) == list(range(1, 16))
    for start, witness in enumerate(WITNESSES):
        block = set(range(start, start + FORBIDDEN_RUN))
        outside = [i for i in range(N) if i not in block]
        block_sum = 0
        for i in block:
            block_sum ^= COLS[i]
        assert all(dot(witness, COLS[i]) == 0 for i in outside)
        assert dot(witness, SYNDROME ^ block_sum) == 1
        print(f'BLOCK {start + 1}: SEPARATION PASS, witness={witness}')

    code = [mask for mask in range(1 << N)
            if syndrome(mask) == SYNDROME]
    assert len(code) == 2048
    assert not any(contains_run(x, FORBIDDEN_RUN) for x in code)
    assert all((a ^ b).bit_count() >= 3 for a, b in combinations(code, 2))
    covered = set()
    for c in code:
        ball = [c] + [c ^ (1 << i) for i in range(N)]
        assert covered.isdisjoint(ball)
        covered.update(ball)
    assert len(covered) == 1 << N
    print('CODEWORDS=2048; FORBIDDEN CODEWORDS=0; COVERED=32768')
    print('NO84 FULL FINITE CERTIFICATE PASS')


if __name__ == '__main__':
    main()
