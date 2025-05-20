# パナソニックグループ プログラミングコンテスト2025（AtCoder Beginner Contest 406）
# C - ~
# https://atcoder.jp/contests/abc406/tasks/abc406_c

N = int(input())
P = list(map(int, input().split()))

# 1. 隣接大小で文字列 S を作る
S = []
for i in range(N - 1):
    if P[i] < P[i + 1]:
        S.append('<')
    else:
        S.append('>')

# 2. ランレングス圧縮
RLE = []
prev = S[0]
count = 1
for i in range(1, len(S)):
    if S[i] == prev:
        count += 1
    else:
        RLE.append((prev, count))
        prev = S[i]
        count = 1
RLE.append((prev, count))

# 3. チルダ型 "<" + ">" + "<" の形を数える
ans = 0
for i in range(1, len(RLE) - 1):
    if RLE[i][0] == '>' and RLE[i - 1][0] == '<' and RLE[i + 1][0] == '<':
        a = RLE[i - 1][1]
        b = RLE[i + 1][1]
        ans += a * b

print(ans)


"""
# 解法ステップ
1. 隣接大小で文字列 S を作る
    - P[i] < P[i+1] なら '<'、そうでなければ '>' を S に追加
2. ランレングス圧縮
    - 同じ記号が連続している部分を (記号, 長さ) のタプルにまとめる
3. チルダ型 "<" + ">" + "<" の形を数える
    - RLEで '<', '>', '<' の3連続のパターンを見つけたとき、左の '<' の長さ a × 右の '<' の長さ b を加算する
"""
