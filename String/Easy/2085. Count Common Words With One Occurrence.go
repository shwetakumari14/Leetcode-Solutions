package main

import (
	"fmt"
	"sync"
)

func main() {

	words1, words2 := []string{"leetcode", "is", "amazing", "as", "is"}, []string{"amazing", "leetcode", "is"}
	result := countWords(words1, words2)
	fmt.Println(result)
}

func countWords(words1 []string, words2 []string) int {

	count := 0

	wordMap1 := make(map[string]int)
	wordMap2 := make(map[string]int)

	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		defer wg.Done()
		for _, val := range words1 {
			wordMap1[val]++
		}
	}()
	go func() {
		defer wg.Done()
		for _, val := range words2 {
			wordMap2[val]++
		}
	}()
	wg.Wait()

	for i := 0; i < len(words1); i++ {
		val1, ok1 := wordMap1[words1[i]]
		val2, ok2 := wordMap2[words1[i]]
		if ok1 && ok2 && val1 == 1 && val2 == 1 {
			count++
		}

	}

	return count
}
