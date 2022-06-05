package main

import (
	"fmt"
	"strings"
)

func main() {
	// Declaring variables
	var input string
	var palindrome []string
	fmt.Println("Enter a palindrome word: ")

	// Take the input of the user
	fmt.Scan(&input)

	// Checks the input if not empty
	if len(input) > 0 {
		// Reverse string and append it to palindrome which is an array of string
		for i := (len(input) - 1); i >= 0 && i < len(input); i-- {
			palindrome = append(palindrome, string(input[i]))
		}
	}

	// Joining character of strings and compare the formed word to the input.
	if strings.Join(palindrome, "") == input {
		fmt.Println("---------------------------------")
		fmt.Printf("Word: %s\nInput: %s\nUser entered a palindrome word\n", strings.Join(palindrome, ""), input)
	} else {
		fmt.Println("Not a palindrome word")
	}
}
