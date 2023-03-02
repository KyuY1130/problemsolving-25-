import sys
T= int(input())
for i in range(T):
  a,b = map(int, sys.stdin.readline().split())
  print(a+b)5
  # sys.stdin.readline()은 input() 대신 사용 가능함.
  # int 자료형으로 변경하면 상관없지만 문자형으로 입력을 받을 경우 개행문자\n 도 문자로 인식한다.