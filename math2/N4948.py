#n에 대해 n 보다 크고 2n
while True:
  n=int(input())
  if n==0:
    break
  sosu=0
  for i in range(n,2n+1):
    if n==1:
      continue
    for j in range(2,(i**0.5)+1)
      if i%j==0:
        break
    else:
      sosu+=1