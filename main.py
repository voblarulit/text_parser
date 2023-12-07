# подготовка текста к анализу

text = input("Введите текст: ").lower()
punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

# анализ текста

char_frequency = {}

for char in text:
    if char.isalpha():
        char_frequency[char] = char_frequency.get(char, 0) + 1

# определение количества разных слов, самого длинного и самого короткого слова
unique_words = set(words)
max_length_word = max(words, key=len)
min_length_word = min(words, key=len)

# вывод результатов

print("Количество разных слов:", len(unique_words))
print("Самое длинное слово:", max_length_word)
print("Самое короткое слово:", min_length_word)

print()

# частота символов
print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")