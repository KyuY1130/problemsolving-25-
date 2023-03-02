n=int(input())
for i in range(n):
  a=list(input())
  b=0
  c=0
  for d in a:
    if d=='O':
      b+=1
      c+=b
    else :
      b=0
  print(c)
