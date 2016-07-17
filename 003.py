# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from sys import argv
fileName, inputNum = argv

def isDivisibleBy (num, listDiv):
	for i in range (len (listDiv)):
		if num % listDiv [i] == 0:
			return True
	return False

def isInList(lst, num):
	for i in range (len(lst)):
		if lst[i] == num:
			return True
	return False

# returns all primes <= a number
def erastosthenes (num):
	lst = range (2, num)
	primesLst = []
	for i in range (math.floor(num**0.5) - 2):
		if lst[i] != 1:
			primesLst.append(lst[i])
			multiple = lst[i]
			n = 1
			while multiple*n < num:
				lst [multiple*n - 2] = 1
				n+= 1
	return primesLst

def findPrimeFactors (num):
	primesToCheck = erastosthenes(num)
	primeFactors = []

	for i in range (len (primesToCheck)):
		if num % primesToCheck[i] == 0:
			primeFactors.append(primesToCheck[i])
	return primeFactors	

def isPrime (num):
	return len (findPrimeFactors(num)) > 0

def findPrimeFactorsOfBigNum (num):
	primesList = []
	i = 2
	while i <= num:
		if (not isInList (primesList, i)) and (not isDivisibleBy (num, primesList)) and num % i == 0:
			primesList.append (i)
			num /= i
		i += 1
	return primesList

def listMax (lst):
	numMax = lst [0]
	for i in range (len (lst)):
		if lst [i] > numMax:
			numMax = lst [i]
	return numMax
		
print listMax(findPrimeFactorsOfBigNum (int(inputNum) ) ) 
	
