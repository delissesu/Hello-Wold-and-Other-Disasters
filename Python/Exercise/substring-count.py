# Auto
word = input().title().strip().split()
find_str = word.count("Delion")
print(find_str)

# Manual
word = "Today is very cold. Really, cold.".lower()
substr = "cold"

len_word = len(word)
len_substr = len(substr)
count = 0

for i in range(len_word - 1):
    count += word[i:i + len_substr] == substr

print(count)