package main

import "fmt"

func main() {

	word, ch := "abcdefd", "d"
	data := []byte(ch)
	result := reversePrefix(word, data[0])
	fmt.Println(result)

}

func reversePrefix(word string, ch byte) string {
	str := []byte(word)
	first, last := 0, 0
	for i := 0; i < len(str); i++ {
		if str[i] == ch {
			last = i
			break
		}
	}
	for first < last {
		str[first], str[last] = str[last], str[first]
		first++
		last--
	}

	return string(str)
}
