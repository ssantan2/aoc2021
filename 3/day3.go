package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	inp_file, _ := os.Open("input1.txt")
	defer inp_file.Close()
	scanner := bufio.NewScanner(inp_file)

	row_count := 0
	var arr [12]int
	for scanner.Scan() {
		row_val := scanner.Text()
		for i := 0; i < len(row_val); i++ {
			int_val, _ := strconv.Atoi(string(row_val[i]))
			arr[i] = arr[i] + int_val
		}
		row_count++
	}

	var rev_arr [12]int
	for i := 0; i < len(arr); i++ {
		if arr[i] < row_count/2 {
			arr[i] = 0
			rev_arr[i] = 1
		} else {
			arr[i] = 1
			rev_arr[i] = 0
		}
	}
	gamma := strings.Trim(strings.Replace(fmt.Sprint(arr), " ", "", -1), "[]")
	gamma_int, _ := strconv.ParseInt(gamma, 2, 64)
	epsilon := strings.Trim(strings.Replace(fmt.Sprint(rev_arr), " ", "", -1), "[]")
	epsilon_int, _ := strconv.ParseInt(epsilon, 2, 64)

	fmt.Println(row_count)
	fmt.Println(gamma_int)
	fmt.Println(epsilon_int)
	fmt.Println(gamma_int * epsilon_int)
}
