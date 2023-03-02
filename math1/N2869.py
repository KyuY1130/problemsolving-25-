A,B,V=map(int,input().split())
#V=A*n-B*(n-1)
s=V-B
t=A-B
if s%t==0:
  print(int(s/t))
else:
  print(int(s/t)+1)

# A, B, V = map(int, input().split())

# x = (V-B)/(A-B)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)