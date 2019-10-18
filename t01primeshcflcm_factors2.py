# Generate a list containing factors of num.

num = 18
actual_num = num
start = 2
prime_fact = []

while start <= num:
if num % start == 0:
  prime_fact += [start]
  num = num / start
  else:
    start += 1
    
print(prime_fact)
   
print(actual_num,end = ' ')
print("=", end=' ')
for index, i in enumerate(prime_factor):
  print(i, end=' ')
  if index, != len(prime_fact)-1:
    print("x", end = ' ')
