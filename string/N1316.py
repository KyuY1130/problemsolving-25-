N =int(input())
count=0
for i in range(N):
  w=input()
  e= 0
  for i in range(len(w)-1):#앞뒤 인덱스가 같은지 다른지를 비교하기 위해서 하나 작게 만들었다.
    if w[i] != w[i+1]:
      nw=w[i+1:]
      if nw.count(w[i]):
        e+=1
  if e==0:
    count+=1
print(count)
      
  

