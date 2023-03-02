X= int(input())#총액
N= int(input())#종류
result=0
for i in range(N):
  a,b = map(int, input().split())
  result += a*b
if X==result:
  print("Yes")
else :
  print('No')

X,N,*A=open(0)
print("YNeos"[int(X)!=sum(eval(i.replace(*' *'))for i in A)::2])