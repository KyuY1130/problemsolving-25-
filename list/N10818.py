N=int(input())
N_list = list(map(int, input().split()))
a = N_list[0]
b = N_list[0]
for i in N_list:
  if i < a :
    a = i
for i in N_list:
  if i > b :
    b = i
print(a,b)
  