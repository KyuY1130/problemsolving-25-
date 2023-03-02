A,B,C=map(int,input().split())
#A+B*n=C*next
if B-C >= 0:
  print(-1)
else:
  print(int(A/(C-B))+1)