# Друге завдання
#
#
#
# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
#
#
#
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
#
#
#
# Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.


from random import sample


def get_numbers_ticket(min: int, max: int, quantity: int):
    """
    Повертає відсортований список унікальних випадкових чисел довжини quantity
    у діапазоні [min, max]. У разі некоректних вхідних даних повертає [].
    """
    # Валідація параметрів
    if (
        not isinstance(min, int)
        or not isinstance(max, int)
        or not isinstance(quantity, int)
        or min < 1
        or max > 1000
        or min >= max
        or quantity <= 0
        or quantity > (max - min + 1)
    ):
        return []

    numbers = sample(range(min, max + 1), quantity)
    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))