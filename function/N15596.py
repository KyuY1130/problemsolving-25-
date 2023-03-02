# a=[]
# for i in range(1,10001):
#   a.append(i)
a=list(range(1,10001))
# c=[]
# for i in range(1,10000):
#   if i>=1000:
#     b=str(i)
#     d=int(b)+int(b[0])+int(b[1])+int(b[2])+int(b[3])
#     if d<=10000:
#       c.append(d)
#   elif i>=100:
#     b=str(i)
#     d=int(b)+int(b[0])+int(b[1])+int(b[2])
#     if d<=10000:
#       c.append(d)
#   elif i>=10 :
#     b=str(i)
#     d=int(b)+int(b[0])+int(b[1])
#     if d<=10000:
#       c.append(d)
#   else:
#     b=str(i)
#     d=int(b)+int(b[0])
#     c.append(d)
c=[]
for i in a:
  for n in str(i):
    i += int(n)
  if i<=10000:
    c.append(i)
list(set(c))
f= [x for x in a if x not in c]
for i in f:
  print(i)