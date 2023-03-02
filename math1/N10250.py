T=int(input())
for i in range(T):  
  H,W,N=map(int,input().split())
#한층의 방 개수 W
#층수 H
#몇 번쨰 손님 N
  a=str(N//H+1)
  b=str(N%H)
  if int(a)<10:
    print(b+'0'+a)
  else:
    print(b+a)

T=int(input())
for i in range(T):  
  H,W,N=map(int,input().split())
#한층의 방 개수 W
#층수 H
#몇 번쨰 손님 N
  a=N//H+1
  b=N%H
  if N%H ==0:
    a=N//H
    b=H
  print(b*100+a)
  
    