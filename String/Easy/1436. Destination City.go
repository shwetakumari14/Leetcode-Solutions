package main

import "fmt"

func main() {

	paths := [][]string{{"London", "New York"}, {"New York", "Lima"}, {"Lima", "Sao Paulo"}}
	result := destCity(paths)
	fmt.Println(result)
}

func destCity(paths [][]string) string {
	destiCity, destMap := "", make(map[string]string)

	for _, val := range paths {
		destMap[val[0]] = val[1]
	}

	for _, val := range destMap {
		_, ok := destMap[val]
		if !ok {
			destiCity = val
		}
	}

	return destiCity
}
