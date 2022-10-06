#!/usr/bin/python3

"""
Python function to test if a given number is a power of two
"""

import sys
from os.path import basename

def main():
	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:
			try:
				x = int(arg)
				is_pwr = 'a' if (x > 0 and (x & (x-1)) == 0) else 'not a'
				print(f"{arg} is {is_pwr} power of two.")
			except:
				print(f"Error: {arg} is not an integer!")
	else:
		print(f"Usage: {basename(sys.argv[0])} <number> [additional numbers]")

if __name__ == '__main__':
	main()
