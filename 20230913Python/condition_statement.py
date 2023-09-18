# print("How old are you?")
# myage = int(input())

# # if입력 후 : 입력. if문 안쪽 내용은 들여쓰기를 한다.
# if myage < 30:
#     print("Welcome to the Club")
# else:
#     print("Oh! No.")

# 비교 연산자
x = 100
y = 150

print(x < y) #x가 y보다 작은지 검사
print(x > y) #x가 y보다 큰지 검사
print(x == y) #x와 y의 값이 같은지 검사
print(x is y) #x와 y의 메모리 주소가 같은지 검사. -5부터 256까지의 정수값은 특정 메모리 주소에 저장.
print(x != y) #x와 y가 값이 같지 않은지 검사
print(x is not y) #x와 y의 메모리 주소가 같지 않은지 검사
print(x >= y) #x가 y보다 크거나 같은지 검사
print(x <= y) #x가 y보다 작거나 같은지 검사

print('-----------------')

# True, False 치환. 컴퓨터는 기본적으로 이진수 처리. true -> 1, false -> 0
if 1:
    print("True")
else:
    print("False")

