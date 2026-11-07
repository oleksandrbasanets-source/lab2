"""Завдання 3. Множина B із множини A та символу x."""


def build_b(a, x):
    """Якщо x відсутній в A — додає його, якщо є — видаляє.
    Видалення з множини виконується через список, як вимагає умова."""
    if x not in a:
        return a | {x}                 # а) додавання елемента x
    items = list(a)                    # б) множину -> список
    items = [c for c in items if c != x]
    return set(items)                  # результат -> знову множина


def print_set(s):
    print("{" + ", ".join(sorted(s)) + "}")


if __name__ == "__main__":
    a = set(input("Введіть символи множини A: ").replace(" ", ""))
    while True:
        x = input("Введіть символ x: ")
        if len(x) == 1:
            break
        print("Помилка: потрібно ввести рівно один символ.")
    print("Множина A:")
    print_set(a)
    print("Множина B:")
    print_set(build_b(a, x))