# トヨタ自動車プログラミングコンテスト2025（AtCoder Beginner Contest 389）
# C - Snake Queue 
# https://atcoder.jp/contests/abc389/tasks/abc389_c

Q = int(input())

lengths = []
prefix_sum = [0]  # 累積長さ
offset = 0  # 全体シフト量

output = []

for _ in range(Q):
    parts = input().split()
    if parts[0] == '1':
        l = int(parts[1])
        lengths.append(l)
        prefix_sum.append(prefix_sum[-1] + l)
    elif parts[0] == '2':
        m = lengths.pop(0)
        prefix_sum.pop(1)  # 先頭を抜く（prefix_sum[0]はダミー）
        offset += m
    elif parts[0] == '3':
        k = int(parts[1])
        # k番目のヘビの頭 = 累積長さ[k-1] - offset
        pos = prefix_sum[k - 1] - offset
        output.append(str(pos))

print('\n'.join(output))

"""
# 問題のポイント
- ヘビの列に対して、追加・削除・位置取得の3種類のクエリを高速に処理する必要がある。
- 各ヘビの頭の位置を都度計算するのは非効率なので、累積和で管理して O(1) で答える工夫が必要。
- 削除による全体の座標移動は offset にまとめて管理することで O(1) に抑える。

# 解法ステップ
1. `lengths` に各ヘビの長さを保持し、`prefix_sum` で累積長さを管理。
2. タイプ1（追加）のたびに、`prefix_sum` に新たな長さを足しておく。
3. タイプ2（削除）のときは、先頭の長さを取り除き、それを offset に加える。
4. タイプ3（k番目のヘビの頭の位置）は、`prefix_sum[k - 1] - offset` で計算可能。
5. クエリ数が多いため、出力はまとめて最後に行う。
"""
