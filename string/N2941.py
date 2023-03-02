a=['c=','c-','dz=','d-','lj','nj','s=','z=']
b=input()

for i in a:
  b = b.replace(i,'_')# 변수명을 다르게 해서 저장해야 원본이 훼손되지 않음.
print(len(b))
#replace 함수 = replace(a,b) a를 b로 대체