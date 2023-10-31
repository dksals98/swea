T = int(input())
palindrome = [0] * (T + 1)

for i in range(1, T + 1):
    word = input()
    word_length = len(word) // 2
    if len(word) % 2 == 1:
        if word[:word_length] == word[:word_length:-1]:
            palindrome[i] = 1
    else:
        if word[:word_length] == word[:word_length - 1:-1]:
            palindrome[i] = 1

for j in range(1, T + 1):
    print(f'#{j} {palindrome[j]}')