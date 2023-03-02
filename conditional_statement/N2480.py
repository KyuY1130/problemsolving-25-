a,b,c = map(int, input().split())
price= 0
if a==b==c :
  price=10000+a*1000
elif a==b or a==c :
  price=1000+a*100
elif b==c :
  price=1000+b*100
else :
  price= min(a,b,c)*100
print(price)

# *_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])