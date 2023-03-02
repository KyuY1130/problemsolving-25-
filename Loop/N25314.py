n=int(input())
for i in range(n):
  print('long '*(n//4+1)+'int')


a = int(input())

while a > 0:
    if a > 4:
         print('long ', end = '')
    else:
         print('long int')
    a = a - 4


import sys

input = sys.stdin.readline

a = int(input())

cnt = a // 4

for i in range(cnt) :
    print("long" , end = ' ')

print('int')
