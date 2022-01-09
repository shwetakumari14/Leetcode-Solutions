package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {

	s, t := "anagram", "nagaram"
	result := isAnagram(s, t)
	fmt.Println(result)
}

func isAnagram(s string, t string) bool {
	str := strings.Split(s, "")
	txt := strings.Split(t, "")

	sort.Strings(str)
	sort.Strings(txt)

	s = strings.Join(str, "")
	t = strings.Join(txt, "")

	if s == t {
		return true
	}
	return false
}
