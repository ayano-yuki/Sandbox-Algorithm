package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Itemは、ナップザックに入れるアイテムを表します
type Item struct {
	weight int // 重さ
	value  int // 価値
}

// Individualは、解の候補（個体）を表します
type Individual struct {
	genes    []int // アイテムの選択状態（0: 選ばない、1: 選ぶ）
	fitness  int   // 適応度（総価値）
}

// パラメータ設定
const (
	populationSize = 100    // 個体群のサイズ
	itemCount      = 5      // アイテム数
	maxWeight      = 50     // ナップザックの最大重量
	mutationRate   = 0.01   // 突然変異率
	crossoverRate  = 0.7    // 交叉率
	maxGenerations = 100    // 最大世代数
)

// ナップザック問題のアイテム（重さと価値）
var items = []Item{
	{weight: 10, value: 60},
	{weight: 20, value: 100},
	{weight: 30, value: 120},
	{weight: 40, value: 150},
	{weight: 50, value: 200},
}

// 個体群をランダムに初期化
func initPopulation() []Individual {
	population := make([]Individual, populationSize)
	for i := 0; i < populationSize; i++ {
		individual := Individual{
			genes: make([]int, itemCount),
		}
		// 各アイテムをランダムに選択（0 または 1）
		for j := 0; j < itemCount; j++ {
			individual.genes[j] = rand.Intn(2)
		}
		population[i] = individual
	}
	return population
}

// 適応度を計算（ナップザック内のアイテムの総価値 - 超過重量があればペナルティ）
func calculateFitness(individual *Individual) {
	totalWeight := 0
	totalValue := 0
	for i := 0; i < itemCount; i++ {
		if individual.genes[i] == 1 { // アイテムが選ばれた場合
			totalWeight += items[i].weight
			totalValue += items[i].value
		}
	}
	// 重量制限を超えていればペナルティをつける
	if totalWeight > maxWeight {
		individual.fitness = -1 // これは無効な解として評価
	} else {
		individual.fitness = totalValue
	}
}

// 2つの親から交叉して子を生成
func crossover(parent1, parent2 Individual) Individual {
	child := Individual{
		genes: make([]int, itemCount),
	}
	if rand.Float64() < crossoverRate {
		crossoverPoint := rand.Intn(itemCount)
		// 交叉ポイントまで親1の遺伝子、残りは親2の遺伝子
		for i := 0; i < crossoverPoint; i++ {
			child.genes[i] = parent1.genes[i]
		}
		for i := crossoverPoint; i < itemCount; i++ {
			child.genes[i] = parent2.genes[i]
		}
	} else {
		child = parent1
	}
	return child
}

// 突然変異を行う
func mutate(individual *Individual) {
	for i := 0; i < itemCount; i++ {
		if rand.Float64() < mutationRate {
			// アイテムを選ぶか選ばないかをランダムに変更
			individual.genes[i] = 1 - individual.genes[i]
		}
	}
}

// 親を選択（トーナメント選択）
func selectParents(population []Individual) (Individual, Individual) {
	// トーナメント選択：ランダムに2個体を選んで、最適な個体を選ぶ
	parent1 := population[rand.Intn(populationSize)]
	parent2 := population[rand.Intn(populationSize)]
	for i := 0; i < 5; i++ {
		candidate := population[rand.Intn(populationSize)]
		if candidate.fitness > parent1.fitness {
			parent1 = candidate
		}
		candidate = population[rand.Intn(populationSize)]
		if candidate.fitness > parent2.fitness {
			parent2 = candidate
		}
	}
	return parent1, parent2
}

// 遺伝的アルゴリズム
func geneticAlgorithm() Individual {
	rand.Seed(time.Now().UnixNano())
	population := initPopulation()

	for generation := 0; generation < maxGenerations; generation++ {
		// 各個体の適応度を計算
		for i := 0; i < populationSize; i++ {
			calculateFitness(&population[i])
		}

		// 最良の個体を探す
		best := population[0]
		for i := 1; i < populationSize; i++ {
			if population[i].fitness > best.fitness {
				best = population[i]
			}
		}

		// 解が見つかった場合
		if best.fitness >= 0 && best.fitness <= 100 {
			fmt.Printf("解が見つかりました！ 世代: %d\n", generation)
			return best
		}

		// 次世代の個体群を作成
		newPopulation := make([]Individual, populationSize)
		for i := 0; i < populationSize; i++ {
			// 親を選択
			parent1, parent2 := selectParents(population)
			// 交叉
			child := crossover(parent1, parent2)
			// 突然変異
			mutate(&child)
			// 新しい個体を追加
			newPopulation[i] = child
		}
		population = newPopulation
	}

	// 最良の個体を返す
	best := population[0]
	for i := 1; i < populationSize; i++ {
		if population[i].fitness > best.fitness {
			best = population[i]
		}
	}
	return best
}

// メイン関数
func main() {
	best := geneticAlgorithm()
	fmt.Println("最適解:")
	fmt.Println("選ばれたアイテム:")
	for i, gene := range best.genes {
		if gene == 1 {
			fmt.Printf("アイテム %d: 重さ %d, 価値 %d\n", i+1, items[i].weight, items[i].value)
		}
	}
	fmt.Printf("総価値: %d\n", best.fitness)
}
