# -*- coding: utf-8 -*-
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from sys import argv
import math, time
fileName, inputNum = argv

def findSumSquareDifference (upToNum):
	sumSquares = 0
	for i in range (1, upToNum + 1):
		sumSquares += i*i

	squareSum = 0
	for i in range (1, upToNum + 1):
		squareSum += i
	squareSum *= squareSum

	return squareSum - sumSquares

tStart = time.time()
print findSumSquareDifference(int(inputNum))
print (str((time.time() - tStart)))