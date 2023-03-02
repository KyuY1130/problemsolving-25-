N=int(input())
numbers = map(int,input().split())
sosu=0
for i in numbers :
  error=0
  if i>1:
    for s in range(2,i):
      if i%s==0:
        error+=1
    if error == 0:
      sosu+=1
print(sosu)