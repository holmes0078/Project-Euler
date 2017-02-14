def main():
  sum1 = 0
  sum2 = 0
  
  for i in range(1,(1000/3)+1):
	if 3*i <= 1000:
		sum1 = sum1 + 3*i
  
  print sum1
  
  for j in range(1,(1000/5)+1):
    if 5*j < 1000:
		sum2 = sum2 + 5*j
  
  print sum2
  
  sum = sum1 + sum2
 
  for k in range(1,(1000/15)+1):
    if 15*k < 1000:
		sum = sum - 15*k

  print sum
  
if __name__ == main():
  main()