# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, number_1, number_2, *args):
        self.number_1 = number_1
        self.number_2 = number_2
        self.complexn = 'number_1 + number_2 * i'

    def __add__(self, other):
        return f'Сумма комплексных чисел равна {self.number_1 + other.number_1} + {(self.number_2 + other.number_2)}*i'

    def __mul__(self, other):
        return f'Сумма комплексных чисел равна {self.number_1 * other.number_1 - self.number_2 * other.number_2} ' \
               f'+ {self.number_1 * other.number_2 + self.number_2 * other.number_1}*i'



complex_number_1 = ComplexNumber(4, 2)
complex_number_2 = ComplexNumber(3, 1)
print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)