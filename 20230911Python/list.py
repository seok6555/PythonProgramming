# 인덱싱
colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[2])
print(len(colors))

# 슬라이싱
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:6]) # 0번째 인덱스부터 6번째 인덱스에 -1한 값인 5번째 인덱스까지 출력.
print(cities[5:]) # 5번째 인덱스부터 끝까지 출력.
print(cities[-8:]) # 리버스 인덱스. -8번째(0번째) 인덱스 부터 끝까지(-1번째) 출력.
print(cities[:]) # 리스트의 처음부터 끝까지 모든 값을 출력.
print(cities[-50:50]) # 인덱스 범위가 넘어가도 알잘딱으로 처음부터 끝까지 범위를 조정하여 출력.

# 증가값
print(cities[::2]) # 2칸 간격으로 출력.
print(cities[::-1]) # 역방향으로 1칸 간격으로 출력. 역으로 슬라이싱.

# 덧셈 연산
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2) # 두 리스트를 합침.
print(len(color1)) # 리스트 길이.
total_color = color1 + color2 # 덧셈 연산을 하더라도 따로 어딘가에 변수 형태로 저장해주지 않으면 기존 변수에 영향x.
print(total_color)

# 곱셈 연산
print(color1 * 2) #color1 리스트 2회 반복.

# in 연산
print('blue' in color2) # color2 변수에 blue가 있으면 True, 없으면 False 출력.

# append() 함수
colors.append('white') # 자바, c#의 list.add의 개념. 리스트 마지막에 해당 값을 새로 추가.
print(colors)

# extend() 함수
colors.extend(['black', 'purple']) # 리스트에 새로운 리스트 추가. 덧셈 연산과 같은 기능.
print(colors)

# insert() 함수
colors.insert(0, 'orange') # 특정 위치에 값 추가.
print(colors)

# remove() 함수
colors.remove('red') # 특정 값 제거.
print(colors)

# 인덱스 재할당, 삭제
colors[0] = 'red' # 0번째에 red를 재할당. 값을 교체하는 개념.
print(colors)
del colors[0] # 0번째 값을 제거.
print(colors)

# 패킹, 언패킹
t = [1, 2, 3] # 1, 2, 3을 변수 t에 패킹.
a, b, c = t # t의 값 1, 2, 3을 a, b, c에 언패킹.
print(t, a, b, c)

# 이차원 리스트
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)