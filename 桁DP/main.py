# AtCoder Beginner Contest 154
# E - Almost Everywhere Zero
# https://atcoder.jp/contests/abc154/tasks/abc154_e

from functools import lru_cache

N = input().strip()
K = int(input())
L = len(N)

@lru_cache(maxsize=None)
def dp(pos: int, count: int, tight: bool):
    if count > K:
        return 0
    if pos == L:
        return 1 if count == K else 0

    res = 0
    limit = int(N[pos]) if tight else 9

    for digit in range(0, limit + 1):
        new_count = count + (1 if digit != 0 else 0)
        new_tight = tight and (digit == limit)
        res += dp(pos + 1, new_count, new_tight)

    return res

print(dp(0, 0, True))

"""
# 問題の要点
- 1 以上 N 以下の整数のうち、10進法で表したときに 0 でない数字がちょうど K 個あるものの個数を求める。
- N は最大で 100 桁弱の非常に大きな数なので、単純な全探索は不可能。
- 非0桁の個数がK個という制約に注目し、桁DP（Digit DP）で数え上げる。

# 解法ステップ
1. 数Nを文字列として受け取り、桁数に基づいてDPを定義する。
2. dp(pos, count, tight) を状態とし、以下の意味で管理する：
   - pos: 現在注目している桁の位置（左から順に）
   - count: 今までに使った0でない数字の個数
   - tight: これまでの桁が N と一致しているか（True ならこの桁の数字は N[pos] 以下に制限）
3. 各桁ごとに 0〜9 の数字を試し、次の状態へ遷移。
   - digit ≠ 0 のとき count を1増やす。
   - digit == N[pos] のときは tight を維持、それ以外は tight=False で自由に選べる状態に遷移。
4. 桁を全て見終わったとき（pos == L）に count == K であれば1を返し、そうでなければ0。
5. すべてのパスを合計することで、条件を満たす数の個数が得られる。
"""