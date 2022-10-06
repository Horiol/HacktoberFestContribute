#!/usr/bin/python3

"""
Python function that calculates the factorial of a given number.
Accepts command line arguments or interactive user input
"""

import sys


def factorial(num):
	try:
		n = int(num)
		res = i = 1
		while i <= n:
			res *= i
			i += 1
		return res
	except Exception as e:
		print(f"Error: {num} is not a number!")


def main():
	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:
			print(f"Factorial of {arg} is: {factorial(arg)}")
	else:
		num = input("Insert a number to find its factorial: ")
		print(f"Factorial of {num} is: {factorial(num)}")

if __name__ == '__main__':
	main()
