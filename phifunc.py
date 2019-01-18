
import time
## this function test wither the number is prime or not
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
## this function to finde prime factors for the number
def fac(n):
	a = []
	for i in range(1,n+1):
		if n%i==0 and is_prime(i):
				k=0
				while n/(i) == int(n/(i)):
					n = int(n/i)
					k=k+1
				a.append((i,k))
				
		if n ==1 : break	
	return a
def phi(n):
	a = fac(n)
	m=1
	for i in a:
		m*=(pow(i[0],i[1])-pow(i[0],i[1]-1))
	return m

def sfac(n):
	a = ''
	for i,j in fac(n):
		print(i,j)
		a += '({}^{})'.format(i,j)
		a += '*'
	return a[0:-1]
