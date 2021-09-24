from collections import Counter

# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

print(f'Количество гласных букв в слове {word}')
count = Counter(word.lower())
print(sum(count[letter] for letter in set('аеиоуюя')))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

print('Первые буквы слов:')
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(f'Усреднённая длина слова в предложении: {sentence}')

len_words = 0
for word in sentence.split():
    len_words += len(word)
print(len_words / len(sentence.split()))