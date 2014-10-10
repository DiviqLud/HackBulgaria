def prime_number_of_divisors(n):
	count = 0
	for i in range(1,n+1):
		if(n % i == 0):
			count+=1
	if(count == 1):
		return "False"
	else:
		for i in range(2,count):
			if(count % i == 0):
				return False
		return True

print(prime_number_of_divisors(9))