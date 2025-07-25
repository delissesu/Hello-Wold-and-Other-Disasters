word = input()
len_word = len(word)

print(f"Original String is {word}.")

for x in range(0, len_word - 1, 2):
    print(f"{word[x]}")