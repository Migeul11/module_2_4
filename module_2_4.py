# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

# Пункты задачи:

# 1. Создайте пустые списки primes и not_primes.
primes = []
not_primes = []

# 2. При помощи цикла for переберите список numbers.
for number in numbers:

    # (делаем исключение для number == 1)
    if number == 1:
        continue

    # 4. Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
    is_prime = True

    # 3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    # 5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
    #    в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# 6. Выведите списки primes и not_primes на экран(в консоль).
print("Primes:", primes)
print("Not Primes:", not_primes)
