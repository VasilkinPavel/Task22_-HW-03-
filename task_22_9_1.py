#   Ввод и проверка соответствия вводимых данных (вводимые данные - целое число, последовательность целых чисел)
def check_data(data):
    entered_data = None
    warning = ''

    while True:
        try:
            if data == 'list':
                entered_data = list(map(int, input('Введите последовательность целых чисел через пробел:').split()))
                print('Введённая последовательность - ', entered_data)

            if data == 'digital':
                entered_data = int(input('Введите любое целое число:'))
                print('Введённое число - ', entered_data)

        except ValueError:
            if data == 'list':
                warning = 'В введённой последовательности не все элементы являются целыми числами'

            if data == 'digital':
                warning = 'Введённое значение не является целым числом'

            print('%s\nСледуйте указаниям!' % warning)

        else:
            return entered_data


#   Сортировка списка по возрастанию (сортировка вставками)
def sort_max(array):
    for i in range(1, len(array)):
        tmp = array[i]
        index = i - 1
        while index >= 0 and tmp < array[index]:
            array[index + 1] = array[index]
            index -= 1
        array[index + 1] = tmp
    return array


#   Двоичный поиск
def binary_search(array, digital):

    #   Проверка - входит ли введённое число в интервал последовательности
    if digital < array[0] or digital > array[-1]:
        print('Введенное число не входит в интервал последовательности')
        return False  # Если число не входит в интервал последовательности (списка) - результат "FALSE"


    #   Бинарный поиск
    minimum = 0
    maximum = len(array)

    while minimum < maximum - 1:

        middle = (minimum + maximum) // 2

        if array[middle] < digital:
            minimum = middle

        else:
            maximum = middle

    return minimum


any_list = check_data('list')
any_digital = check_data('digital')

any_list = sort_max(any_list)
print('Список, отсортированный по возрастанию (сортировка вставками):', any_list)

print('Индекс числа, которое меньше введённого, а следующее за введённым - равно или больше введённого:',
      binary_search(any_list, any_digital))