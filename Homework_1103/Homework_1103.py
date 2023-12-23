import random
import time

# random 패키지를 import해서 만든 0에서 100,000까지의 정수 10,000개 리스트.
random_list = [random.randrange(0, 100001) for i in range(10000)]

# 리스트 컴프리헨션 기법을 이용한 최소값.
start = time.time()
minimum = min([i for i in random_list])
end = time.time()
print("리스트 컴프리헨션에 의한 최소값:", minimum)
print("소요 시간:", end - start, "초")

# 함수를 사용하지 않은 반복문을 이용한 최소값.
start = time.time()
minimum = random_list[0]
for i in range(1, len(random_list)):
    if minimum > random_list[i]:
        minimum = random_list[i]
end = time.time()
print("반복문에 의한 최소값:", minimum)
print("소요 시간:", end - start, "초")

# 내장함수를 이용한 최소값.
start = time.time()
minimum = min(random_list)
end = time.time()
print("내장함수에 의한 최소값:", minimum)
print("소요 시간:", end - start, "초")

# 함수내에서 반복문을 사용한 함수 정의 및 호출을 이용한 최소값.
start = time.time()
def operator(r_l):
    result = r_l[0]
    for i in range(1, len(r_l)):
        if result > r_l[i]:
            result = r_l[i]
    return result
minimum = operator(random_list)
end = time.time()
print("함수 정의에 의한 최소값:", minimum)
print("소요 시간:", end - start, "초")

# 리스트 컴프리헨션 기법을 이용한 최대값.
start = time.time()
maximum = max([i for i in random_list])
end = time.time()
print("리스트 컴프리헨션에 의한 최대값:", maximum)
print("소요 시간:", end - start, "초")

# 함수를 사용하지 않은 반복문을 이용한 최대값.
start = time.time()
maximum = random_list[0]
for i in range(1, len(random_list)):
    if maximum < random_list[i]:
        maximum = random_list[i]
end = time.time()
print("반복문에 의한 최대값:", maximum)
print("소요 시간:", end - start, "초")

# 내장함수를 이용한 최대값.
start = time.time()
maximum = max(random_list)
end = time.time()
print("내장함수에 의한 최대값:", maximum)
print("소요 시간:", end - start, "초")

# 함수내에서 반복문을 사용한 함수 정의 및 호출을 이용한 최대값.
start = time.time()
def operator(r_l):
    result = r_l[0]
    for i in range(1, len(r_l)):
        if result < r_l[i]:
            result = r_l[i]
    return result
maximum = operator(random_list)
end = time.time()
print("함수 정의에 의한 최대값:", maximum)
print("소요 시간:", end - start, "초")

# 리스트 컴프리헨션 기법을 이용한 총합.
start = time.time()
total = sum([i for i in random_list])
end = time.time()
print("리스트 컴프리헨션에 의한 총합:", total)
print("소요 시간:", end - start, "초")

# 함수를 사용하지 않은 반복문을 이용한 총합.
start = time.time()
total = 0
for i in random_list:
    total += i
end = time.time()
print("반복문에 의한 총합:", total)
print("소요 시간:", end - start, "초")

# 내장함수를 이용한 총합.
start = time.time()
total = sum(random_list)
end = time.time()
print("내장함수에 의한 총합:", total)
print("소요 시간:", end - start, "초")

# 함수내에서 반복문을 사용한 함수 정의 및 호출을 이용한 총합.
start = time.time()
def operator(r_l):
    result = 0
    for i in r_l:
        result += i
    return result
total = operator(random_list)
end = time.time()
print("함수 정의에 의한 총합:", total)
print("소요 시간:", end - start, "초")

# 리스트 컴프리헨션 기법을 이용한 평균값.
start = time.time()
average = sum([i for i in random_list]) / len(random_list)
end = time.time()
print("리스트 컴프리헨션에 의한 평균값:", average)
print("소요 시간:", end - start, "초")

# 함수를 사용하지 않은 반복문을 이용한 평균값.
start = time.time()
total = 0
for i in random_list:
    total += i
average = total / len(random_list)
end = time.time()
print("반복문에 의한 평균값:", average)
print("소요 시간:", end - start, "초")

# 내장함수를 이용한 평균값.
start = time.time()
average = sum(random_list) / len(random_list)
end = time.time()
print("내장함수에 의한 평균값:", average)
print("소요 시간:", end - start, "초")

# 함수내에서 반복문을 사용한 함수 정의 및 호출을 이용한 평균값.
start = time.time()
def operator(r_l):
    result = 0
    for i in r_l:
        result += i
    result = result / len(r_l)
    return result
average = operator(random_list)
end = time.time()
print("함수 정의에 의한 평균값:", average)
print("소요 시간:", end - start, "초")