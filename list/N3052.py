a=[]
for i in range(10) :
  i =int(input())
  a.append(i%42)
a= set(a) # set은 집합 자료형으로 중복을 제거하는 필터 역할을 함.
print(len(a))