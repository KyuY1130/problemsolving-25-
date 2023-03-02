a= int(input())
for _ in range(a):  
  b= list(map(int, input().split()))
  avg=sum(b[1:])/b[0]
  count=0
  for i in b[1:]:
    if i > avg :
      count+=1
  c=(count/b[0])*100
  print(f'{c:.3f}%')

  #for i in[*open(0)][1:]:a,*b=map(int,i.split());print(f'{sum(a*j>sum(b)for j in b)/a:.3%}')
  