# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class DivisionZero:

    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division(dividend, divider):
        try:
            private = dividend / divider
            return private
        except ZeroDivisionError:
            return f'Деление на ноль невозможно!'

print(DivisionZero.division(100, 10))
print(DivisionZero.division(100, 0))
