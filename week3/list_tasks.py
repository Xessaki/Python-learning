def user_numbers():
    numbers = []
    for number in range(4):
        number = int(input('Введите число'))
        numbers.append(number)
    return numbers

def find_max(lst):
    max_number = 0
    for number in lst:
        max_number += number
    return max_number

numbers = user_numbers()
print(f'Список {numbers}')
print(f'Максимум {find_max(numbers)}')