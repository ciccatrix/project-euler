from sys import argv
fileName, num = argv

def maxPrimeFactor (num):
	maxpf = 2
	i = 2
	while i <= num:
		if num % i == 0:
			if i > maxpf:
				maxpf = i
			while num%i == 0:
				num /= i
		i += 1
		print num
	return maxpf

print maxPrimeFactor (int(num))
