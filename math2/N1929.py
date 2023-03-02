m,n=map(int,input().split())
print(m,n)
for i in range(m,n+1):
  err=0
  if i>1:  
    for s in range(2,i):
      if i%s==0:
        err+=1
  if err==0:
    print(i)

m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)

  def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)