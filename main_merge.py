def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Разделяем массив на левую половину
        right_half = arr[mid:]  # Разделяем массив на правую половину

        merge_sort(left_half)  # Рекурсивно сортируем левую половину
        merge_sort(right_half)  # Рекурсивно сортируем правую половину

        i = j = k = 0

        # Сравниваем элементы и сливаем обратно в основной массив
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы в левой половине
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Проверяем, остались ли элементы в правой половине
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Исходный массив:", array)
    merge_sort(array)
    print("Отсортированный массив:", array)