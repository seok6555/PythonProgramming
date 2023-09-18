tableNumber = input("구구단 몇 단을 계산할까?")

print("구구단", tableNumber, "단을 계산한다.")

for i in range(1, 10):
    result = int(tableNumber) * i
    print(tableNumber, 'x', i, '=', result)