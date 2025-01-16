# HHKBプログラミングコンテスト2025(AtCoder Beginner Contest 388)
# D - Coming of Age Celebration
# https://atcoder.jp/contests/abc388/tasks/abc388_d

N = int(input())
A = list(map(int, input().split()))

# imos法
diff = [0] * (N+1)
for i, a in enumerate(A):
    # imos法はココ
    present = min(a, N-i-1)         # 渡せる数の確認（全部 or 成人の人数　の値をminで取得）
    A[i] -= present                 # 数をpresent分減らす
    diff[i+1]+=1                    # 数を乗算
    diff[min(N, i+1+present)] -= 1  # 渡せる最終地点に減算
    diff[i + 1] += diff[i]          # いまの渡せる数を次に移動

    if i + 1 < N:                   
        a[i + 1] += diff[i + 1]     # 人に数を渡す

print(*A)

"""　解説（）
diff[i+1]+=1                    # 数を乗算
diff[min(N, i+1+present)] -= 1  # 渡せる最終地点に減算
diff[i + 1] += diff[i]          # いまの渡せる数を次に移動

1. 渡す数は一人に付き1つまでなので、それを利用して、次の人に数を渡し、渡せなくなる地点に-1をする。
2. 現状渡せる数を次に引き継ぐ。ここで、減算した数と現状の数が計算され、次に渡せる数が決定する。
この処理のおかげで、疑似的にくり替え処理で数を渡す処理ができる
"""