# ProjectEuler_problem0001

## Problem 1: Multiples of 3 and 5

**The Problem:** Find the sum of all the multiples of 3 or 5 below 1000.

**The Strategy:** Instead of checking every number one by one, I used a mathematical formula for the sum of an arithmetic series. This makes the code much faster, especially for larger numbers.

**Logic:** Total = (Sum of multiples of 3) + (Sum of multiples of 5) - (Sum of multiples of 15)

# ProjectEuler_problem0002

## Problem 2: Even Fibonacci Numbers

**The Problem:** By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

**The Strategy:** Transverse through a list containing all fibonacci numbers whose value donot exceed 4 million and filter even numbers out and add it to the toal sum

**Logic:** sum = sum + (even fibonacci number whose value doesn't exceed 4 million)

## Problem 3: Largest Prime Factor

**The Problem:** What is the largest prime factor of the number 600851475143

**The Strategy:** Continuously divide the number by the smallest possible factor starting from 2, removing each factor as it appears, until the remaining number itself is the largest prime factor.

**Logic:** Keep checking for numbers starting from 2, that can divide the number and do that until i^2 becomes greater than the number

## Problem 4: Largest Palindrome ProductThe Problem: Find the largest palindrome made from the product of two 3-digit numbers.

**The Strategy:** Use top-down generation. Instead of checking all products, construct 6-digit palindromes starting from 999,999 and work downwards. The first one that can be factored into two 3-digit numbers is the answer
.
**Logic:** The algorithm generates palindromes by mirroring 3-digit integers starting from 999 and checks if they can be factored into two 3-digit numbers. For each palindrome, it tests divisors from 999 down to the square root of the palindrome; if a divisor is found and the resulting quotient is also a 3-digit number, the search immediately terminates and returns that palindrome.












