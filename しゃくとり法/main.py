# AtCoder Beginner Contest 395
# C - Shortest Duplicate Subarray
# https://atcoder.jp/contests/abc395/tasks/abc395_c

N = int(input())
A = list(map(int, input().split()))

last_seen = {}
min_len = float('inf')

left = 0
for right in range(N):
    val = A[right]
    if val in last_seen and last_seen[val] >= left:
        # 重複が見つかった場合
        min_len = min(min_len, right - last_seen[val] + 1)
        # 左端を更新
        left = last_seen[val] + 1
    # 現在の要素の最新位置を記録
    last_seen[val] = right

print(min_len if min_len != float('inf') else -1)

"""
# 問題のポイント
長さ N の整数列 A において、同じ値を2回以上含むような **連続部分列** を見つける。
そのような部分列のうち、**最も短い長さ**を求める。
存在しない場合は -1 を出力。

制約が大きいため、O(N^2) は不可。**線形時間（O(N)) のアルゴリズムが必要**。

# 解法ステップ
1. 右端ポインタ `right` を 0 から N-1 まで動かしながらスライディングウィンドウを展開。
2. 各値の **直近の出現位置** を `last_seen` に記録。
3. 同じ値がウィンドウ内に再出現したら、直近の出現位置を用いて長さを計算。
4. 重複を含む部分列の長さを `min_len` に記録し、**左端 `left` を更新**してウィンドウを保つ。
5. 全体の最短長を出力。見つからなければ `-1`。
"""
