package main

import "fmt"

func main() {

	txt, pat := "ABABDABACDABABCABAB", "ABABCABAB"
	result := KMPSearch(pat, txt)
	fmt.Println(result)
}

func KMPSearch(pat, txt string) int {
	m, n, i, j := len(pat), len(txt), 0, 0

	lps := prepareLPS(pat, m, n)

	for i < n {
		if pat[j] == txt[i] {
			i += 1
			j += 1
		}

		if j == m {
			return i - j
		} else if i < n && pat[j] != txt[i] {
			if j != 0 {
				j = lps[j-1]
			} else {
				i += 1
			}
		}
	}

	return -1
}

func prepareLPS(pat string, m, n int) []int {
	len := 0
	lps := make([]int, n)
	i := 1

	for i < m {
		if pat[i] == pat[len] {
			len += 1
			lps[i] = len
			i += 1
		} else {
			if len != 0 {
				len = lps[len-1]
			} else {
				lps[i] = 0
				i += 1
			}
		}
	}

	return lps
}
