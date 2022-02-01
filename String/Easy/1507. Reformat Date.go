package main

import (
	"fmt"
	"strings"
)

func main() {

	date := "20th Oct 2052"
	result := reformatDate(date)
	fmt.Println(result)
}

func reformatDate(date string) string {
	str := strings.Split(date, " ")

	var monthMap = map[string]string{"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

	day := str[0]
	day = day[:len(day)-2]
	if len(day) == 1 {
		day = "0" + day
	}

	month := monthMap[str[1]]
	year := str[2]

	return year + "-" + month + "-" + day

}
