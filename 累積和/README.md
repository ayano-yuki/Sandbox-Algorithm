# 累積和
累積和は、配列の部分和を高速に計算するためのアルゴリズムである。特に、何度も区間の合計を求めるような問題に対して有効となる。

## 概要
### 目的
- 配列の任意の区間 `[l, r]` の合計を O(1) で求める。
- 計算を高速化し、TLE（Time Limit Exceeded）を防ぐ。
- 区間の総和・移動平均・差分計算などに応用可能である。

### キーポイント
- 累積和配列を事前に一度だけ O(n) で作成する。
- 区間 `[l, r]` の和は `prefix[r+1] - prefix[l]` で求められる。
- 配列の先頭にダミーの 0 を入れることで、数式がシンプルになる。

### 計算量
- 累積和配列の構築：O(n)
- 区間和クエリ：O(1)

### アルゴリズムの流れ
1. 累積和配列 `prefix_sum` を作る。
    - `prefix_sum[0] = 0`
    - `prefix_sum[i+1] = prefix_sum[i] + a[i]`
2. 区間 `[l, r]` の合計を求めたいとき：
    - `sum = prefix_sum[r+1] - prefix_sum[l]`
3. 必要に応じて、先頭要素やオフセット（全体への加算・減算）を導入して工夫する。

### 参考になりそう
- [累積和を何も考えずに書けるようにする！](https://qiita.com/drken/items/56a6b68edef8fc605821)
- [競技プログラミングでも使用するアルゴリズム・データ構造の紹介「累積和」編](https://dxo.co.jp/blog-archives/archives/10913)
- [累積和 | 備忘録](https://koseki2580.github.io/study-docs/docs/Algorithm/cumulative-sum/)
- [【第6回】累積和で高速処理をしてみよう](https://blog.maximum.vc/blog/2023/intro-course/6/)
- [競プロの基本事項確認~累積和といもす法~](https://qiita.com/DaikiSuyama/items/67547e14b47cd6360252)
- [競技プログラミングにおけるimos法・累積和問題まとめ](https://blog.hamayanhamayan.com/entry/2017/07/04/020117)