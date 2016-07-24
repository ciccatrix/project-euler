#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from sys import argv
import math, time
fileName, inputNum = argv

def remainderFromFactors (num, factors):
	for i in range (len (factors)):
		temp = num
		if temp % factors [i] == 0:
			num /= factors [i]

	return num

def findSmallestMultiple (upToNum):
	factors = [2]
	for i in range (2, upToNum + 1):
		remainder = remainderFromFactors(i, factors)
		if remainder != 0:
			factors.append(remainder)
	num = 1
	for i in range (len(factors)):
		num = num * factors[i]

	return num

tStart = time.time()
print findSmallestMultiple(int(inputNum))
print (str((time.time() - tStart)))