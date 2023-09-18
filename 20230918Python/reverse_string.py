sentence = input("뒤집을 문자를 입력하세요.")
reverse_sentence = ' '
for char in sentence:
    reverse_sentence = char + reverse_sentence
print(reverse_sentence)