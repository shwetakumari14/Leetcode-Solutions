package main

import "fmt"

func main() {

	items := [][]string{{"qqqq", "qqqq", "qqqq"}, {"qqqq", "qqqq", "qqqq"}, {"qqqq", "qqqq", "qqqq"}, {"qqqq", "qqqq", "qqqq"}, {"qqqq", "qqqq", "qqqq"}, {"qqqq", "qqqq", "qqqq"}, {"qqqq", "qqqq", "qqqq"}}
	ruleKey, ruleValue := "name", "qqqq"
	result := countMatches3(items, ruleKey, ruleValue)
	fmt.Println(result)

}

func countMatches1(items [][]string, ruleKey string, ruleValue string) int {
	var index, count int
	switch ruleKey {
	case "type":
		index = 0
	case "color":
		index = 1
	case "name":
		index = 2
	}

	for _, item := range items {
		for key, val := range item {
			if key == index && val == ruleValue {
				count++
			}
		}
	}

	return count

}

func countMatches2(items [][]string, ruleKey string, ruleValue string) int {
	var count int
	indexMap := map[string]int{"type": 0, "color": 1, "name": 2}

	for i := 0; i < len(items); i++ {
		if items[i][indexMap[ruleKey]] == ruleValue {
			count++
		}
	}

	return count

}

func countMatches3(items [][]string, ruleKey string, ruleValue string) int {
	var count int

	for _, item := range items {
		if ruleKey == "type" && item[0] == ruleValue {
			count++
		} else if ruleKey == "color" && item[1] == ruleValue {
			count++
		} else if ruleKey == "name" && item[2] == ruleValue {
			count++
		}
	}

	return count

}
