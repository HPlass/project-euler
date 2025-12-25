"""
Project Euler Problem 1
Multiples of 3 or 5

Problem:
Find the sum of all the natural numbers below 1000 that are multiples of 3 or 5.

Approach:
- Iterate through numbers from 0 to 999
- Check if each number is divisible by 3 or 5
- Add qualifying numbers to a running total
"""

def sum_of_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    print(sum_of_multiples(1000))