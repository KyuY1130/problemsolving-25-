A= int(input())
Count=0
C=A
while True:
  a= C//10
  b= C%10
  B= a+b
  C = (C%10)*10+B%10
  Count+=1
  if C==A:
    break;
print(Count)

# a=n=int(input());c=1
# while(a:=a%10*10+a*11//10%10)-n:c+=1
# print(c)