# Chapter03-3
# 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foober', 3, 4, False, 3.14159]


# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1]))
print()

# 출력값
"""
d -  <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captine']
d -  10000
d -  21000
d -  Captine
d -  Base
d -  ['B', 'a', 's', 'e']
"""

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3]) # 3 - 1 

# 출력값
"""
d -  [1000, 10000, 'Ace']
d -  ['Ace', 'Base', 'Captine']
e -  ['Base', 'Captine']
"""

# 리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))
print()

# 출력값
"""
c + d [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captine']
c * 3 [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
'Test' + c[0] Test70
"""

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# 출력값
"""
True
[70, 75, 80, 85]
[70, 75, 80, 85]
"""

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))


# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [[ 'a', 'b', 'c' ]]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 끝 부분에 데이터를 삽입할 때
print('a - ', a)
a.sort() # 정렬
print('a - ', a)
a.reverse() # 역순
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # 원하는 위치에 데이터 추가
print('a - ', a)

a.reverse() # 역순
print('a - ', a)
# del a[6]
a.remove(10)
print('a - ', a)
print('a - ', a.pop()) #마지막 글자를 꺼내온다.
print('a - ', a)
print('a - ', a.count(4)) #4의 갯수가 1개가 있다. 몇개의 중복값이 있는지

ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove -> 내가 원하는 값 바로 삭제
#       pop -> 끝에 있는 걸 제거
#       del -> 인덱스 번호를 알고 삭제 