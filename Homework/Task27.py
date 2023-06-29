# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# sentence = str(("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells").upper())
# print(sentence)
# new_sentence = set(sentence.split())
# print(new_sentence)
# print(len(new_sentence))

from string import punctuation

text = " вот текст с презентации: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

for ch in punctuation + r'\n':
    text = text.replace(ch, '')

word = text.lower().split()
different_words_counter = len(set(word))
print(different_words_counter)