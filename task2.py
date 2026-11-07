"""Завдання 2. Видалення зі списку повторень."""


def remove_duplicates(items):
    """Повертає новий список без повторень (порядок збережено)."""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def print_list(items):
    print("[" + ", ".join(items) + "]")


if __name__ == "__main__":
    data = input("Введіть елементи списку через пробіл: ").split()
    print("Початковий список:")
    print_list(data)
    print("Список без повторень:")
    print_list(remove_duplicates(data))