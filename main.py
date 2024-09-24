from collections import Counter


def count_common_elements(*lists):
    """Возвращает количество одинаковых элементов среди всех списков."""
    if not lists:
        return 0

    # Объединяем все списки в один и считаем частоту элементов
    combined = Counter(lists[0])
    for lst in lists[1:]:
        combined &= Counter(lst)

    # Возвращаем общее количество общих элементов
    return sum(combined.values())


if __name__ == "__main__":
    # Пример использования
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 7, 8, 9]
    result = count_common_elements(list1, list2, list3)
    print(f"Количество одинаковых элементов: {result}")
