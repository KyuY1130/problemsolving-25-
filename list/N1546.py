n= int(input())
m = list(map(int, input().split()))
a=[]
for i in range(len(m)):
  a.append((m[i]/max(m))*100)
sum=0
for i in range(len(a)):
  sum += a[i]
sum1=sum/n
print(sum1)


# n,*l=map(int,open(0).read().split())
# print(sum(l)*100/max(l)/n)