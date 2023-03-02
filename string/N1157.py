w=input().upper()
#upper 함수 입력된 영문을 전부 대문자로
#lower 함수 입력된 영문을 전부 소문자로
wl=list(set(w))
#w의 중복값을 제거하고 먼저 나온 값 순서로 만들어진 list 생성
nl=[]
#빈 리스트

for x in wl:
  nl.append(w.count(x))
  #wl에 각 문자별 등장 횟수를 적은 새 리스트 작성
if nl.count(max(nl))>1:
  print('?')
  #count와 max 함수로 최대값이 여러개인 경우 ? 출력
else:
  m=nl.index(max(nl))
  print(wl[m])
  #nl과 wl의 인덱스가 같은것을 이용해 최대값 출력