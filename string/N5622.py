a=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b=list(input().upper())
time=0
for i in a:
  for s in i:
    for x in b:
      if s==x:
        time += a.index(i)+3
print(time)