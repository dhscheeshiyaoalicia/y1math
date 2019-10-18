# Find the Lowest Common Multiple (LCM) of 18 and 30.

# Get the list of factors of b
for i in range(2,b+1):
  if b % i == 0:
    factors_b = factors_b + [i]
    
print(factors_a)
print(factors_b)

common_factors = []
for i in factors_a:
  if i in factors_b:
    common_factors = common_factors + [i]
    
print(common_factors)

hcf = max (common_factors)
print(hcf)

lcm = a+b / hcf
print("lowest common multiple of", a, "and", b, "is:", int(lcm))
