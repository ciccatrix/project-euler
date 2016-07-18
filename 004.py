# coding=utf-8
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

from sys import argv
import math, time
fileName, inputNum = argv

def isPalindrome (num):
	saveNum = num

	reverse = 0
	while num > 0:
		reverse *= 10
		reverse += num % 10
		num = int(num/10)

	return saveNum == reverse

#this the dumb way :>
def isPalindrome2 (num):
	numDig = math.ceil (math.log10 (num))
	digList = [] 

	while numDig > 0: 
		digList.append(math.floor (num / 10**(numDig-1)))
		num -= digList[len(digList) - 1] * 10**(numDig-1)
		numDig-= 1

	checkDig = 0
	numDig = len(digList)

	while checkDig <= math.floor (numDig/2):
		if (digList [checkDig] != digList[numDig-checkDig-1]):
			return False
		checkDig += 1
	return True

def findLargestPalindrome (numDig):
	biggest = 10**(2*(numDig-1))
	numMin = 10**(numDig-1)
	numMax = 10**numDig - 1

	num1 = num2 = numMin

	for num1 in range (numMax, numMin - 1, -1):
		for num2 in range (numMax, numMin - 1, -1):
			if num2 < num1:
				break
			product = num1*num2
			if (product > biggest):
				if isPalindrome(product):
					biggest = product
	return biggest

tStart = time.time()
print findLargestPalindrome(int(inputNum))
print (str((time.time() - tStart)))