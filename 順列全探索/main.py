# トヨタ自動車プログラミングコンテスト2023#2(AtCoder Beginner Contest 302)
# C - Almost Equal
# https://atcoder.jp/contests/abc302/tasks/abc302_c

from itertools import permutations

def differ_by_one(s1, s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

N, M = map(int, input().split())
S = [input() for _ in range(N)]

for perm in permutations(S):
    ok = True
    for i in range(N - 1):
        if not differ_by_one(perm[i], perm[i+1]):
            ok = False
            break
    if ok:
        print("Yes")
        break
else:
    print("No")

"""
# 問題の要点
- N個の文字列 S_1, S_2, ..., S_N（それぞれ長さM）がある。
- これらを並び替えた列 T_1, T_2, ..., T_N を作る。
- 隣り合う文字列 T_i と T_{i+1} は「ちょうど1文字だけ違う」必要がある。


# 解法ステップ
1. 「1文字だけ違うか」を判定する関数を作る
    - 2つの文字列 s1 と s2 の長さは M。
    - 同じ位置にある文字を比較し、異なる文字の個数を数える。
    - 異なる文字がちょうど1つなら条件を満たす。
    - それ以外はダメ。
2. 全ての文字列の順列を試す
    - N個の文字列の並び替え（順列）をすべて列挙する。
    - Pythonでは itertools.permutations(S) が順列を生成するのに便利！（順列全探索）
    - 順列は、N!通りあるため、Nが8以下なら全探索が現実的。

# 結論
- 順列全探索は便利だけど、ABCではあまり使えなそう...
"""