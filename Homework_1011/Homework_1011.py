# random 패키지 import.
import random

# 최소값, 최대값, 총합, 평균값을 구하는 함수 작성.
def operator(randomList):
    # 리스트 오름차순 정렬.
    randomList.sort()
    # 최소값. 오름차순 정렬 후 가장 첫번 째 원소가 최소값.
    minimum = randomList[0]
    # 최대값. 오름차순 정렬 후 가장 마지막 원소가 최대값.
    maximum = randomList[9]
    # 총합
    total = 0
    for i in randomList:
        total += i
    # 평균값
    average = total / 10

    result = {'minimum': minimum, 'maximum': maximum, 'total': round(total, 1), 'average': round(average, 1)}
    return result

number = list(0 for i in range(10))

# 0에서 100까지의 실수 10개를 생성하여 리스트에 저장.
for i in range(10):
    number[i] = round(random.uniform(0, 100), 1)

print('난수로 생성한 수의 리스트:', number)

# 최소값, 최대값, 총합, 평균값을 구하는 함수 호출. 위에서 생성한 리스트를 인수로 전달. 함수는 한번만 호출.
resultList = operator(number)

# 최소값, 최대값, 총합, 평균값을 화면에 출력. 실수는 소수점 이하 첫째자리까지 표시.
print('최소값:', resultList['minimum'])
print('최대값:', resultList['maximum'])
print('총합:', resultList['total'])
print('평균값:', resultList['average'])