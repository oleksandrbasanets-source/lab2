"""Завдання 1. Кількість слів у реченні, що закінчуються на літеру «р»."""
import string


def count_words_ending_with_r(sentence):
    words = [w.strip(string.punctuation + "«»“”—–…") for w in sentence.split()]
    words = [w for w in words if w]
    count = sum(1 for w in words if w.lower().endswith("р"))
    return len(words), count


if __name__ == "__main__":
    while True:
        text = input("Введіть речення (щонайменше 7 слів): ")
        total, count = count_words_ending_with_r(text)
        if total < 7:
            print(f"Помилка: введено слів — {total}, потрібно щонайменше 7.")
            continue
        break
    print(f"Усього слів: {total}")
    print(f"Слів, що закінчуються на літеру «р»: {count}")