user_input = int(input("구구단 몇 단을 계산할까요(2~9)? "))

while(True):
  if not(2 <= user_input <= 9):
    user_input = int(input("잘못 입력했습니다. 2부터 9 사이 숫자를 입력하세요. "))
    continue
  else:
    print("구구단", user_input, "단을 계산합니다.")
    for i in range(1, 10):
      result = user_input * i
      print(user_input, "x", i, "=", result)
    break