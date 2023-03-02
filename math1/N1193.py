x=int(input())
sum=0
i=1
while x>sum:
  sum+=i
  i+=1
s=sum-x+1
if i%2==0:
  print(s, '/',i-s, sep='')
else:
  print(i-s, '/',s, sep='')