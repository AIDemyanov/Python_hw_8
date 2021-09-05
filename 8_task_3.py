# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class ErrorList:

    def __init__(self, *args):
        self.list = []

    def data(self):
        while True:
            try:
                input_list = int(input('Введите число и нажмите enter, чтобы число попало в список или введите значение '
                                       'отличное от числа, чтобы попасть на команду для выхода - '))
                self.list.append(input_list)
                print(f'Введённый список {self.list}')
            except:
                print(f'Вы ввели недопустимое значение (строку или булевео). Попробуйте снова ввести число')
                continuation = input('Чтобы продолжить введите "start" или любое значение, чтобы выйти - ')
                if continuation == 'start':
                    ErrorList(1)
                else:
                    return f'Программа закончена!!!'

error = ErrorList(1)
print(error.data())

