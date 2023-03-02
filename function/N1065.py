# n=int(input())
# k=0
# for i in range(1,n+1) :
#   a=list(map(int,str(i)))
#   if i<100:
#     k+=1
#   elif a[0]-a[1]==a[1]-a[2]:
#     k+=1
# print(k)

def hansu(num):
  k=0
  for i in range(1,num+1) :
    a=list(map(int,str(i)))
    if i<100:
      k+=1
    elif a[0]-a[1]==a[1]-a[2]:
      k+=1
  return k
n=int(input())
print(hansu(n))

#print(sum(i<100or i//100*21+i==i//10*12for i in range(1,int(input())+1)))