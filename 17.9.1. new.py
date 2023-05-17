list1 = input("Введите числа последовательности через пробел: ")
string_list = list1.split()
numbers = list(map(float, string_list))

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Введенные числа:", numbers)
element = float(input("Введите число : "))

def binary_search(numbers, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if numbers[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < numbers[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(numbers, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(numbers, element, middle + 1, right)

index_element = binary_search(numbers, element, 0, len(numbers)-1)
index_element_left = index_element - 1
if index_element_left >= 0:
    print("Индекс первого числа: ",index_element_left)
else:
    print("False")

