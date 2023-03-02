#프로그래밍 언어에서 map은 고차함수로, 전해진 함수를 모든 배열에 적용하여 그 결과를 전달한다.
# 예를 들어, square라는 함수를 만든 뒤 map(square, [1,2,3,4,5])라고 호출한다면 [1,4,9,16,25]를 반환한다.
#이 때, map은 배열을 지나면서 모든 요소에 대하여 squre함수를 적용한다.
###아래는 맵의 사용 예
# T = int(input())
# for i in range(T):
#  A,B = map(int, input().split())
#  print(A+B)

# import sys
# T= int(input())
# for i in range(T):
#  a,b = map(int, sys.stdin.readline().split())
#  print(a+b)5

# X= int(input())#총액
# N= int(input())#종류
# result=0
# for i in range(N):
#  a,b = map(int, input().split())
#  result += a*b
# if X==result:
#  print("Yes")
# else :
#   print('No')

# a,b,c = map(int, input().split())
# price= 0
# if a==b==c :
#   price=10000+a*1000
# elif a==b or a==c :
#   price=1000+a*100
# elif b==c :
#   price=1000+b*100
# else :
#   price= min(a,b,c)*100
# print(price)