# find the sum of the even-valued terms of the Fibonacci 
# sequence whose values do not exceed 4 million
prev = 1 # n-1
curr = 2 # n
evenSum = 0

while curr < 4000000 and prev < 4000000:
	if curr % 2 == 0:
		evenSum += curr
	temp = curr
	curr = prev + curr
	prev = temp

print evenSum
