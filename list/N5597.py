a =[i for i in range(1,31)]

for i in range(28):
  i= int(input())
  a.remove(i) #소거
print(min(a))
print(max(a))
  
# print(*sorted({*range(1,31)}-{*map(int,open(0))}))