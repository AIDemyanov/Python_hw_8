# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Storage:
    pass

class OfficeEquipment:

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

class Printer(OfficeEquipment):

    def __init__(self, model, color, price, speed_print):
        self.model = model
        self.color = color
        self.price = price
        self.speed_print = speed_print

    def action(self):
        return f'{self.model} печатает'

class Scanner(OfficeEquipment):

    def __init__(self, model, color, price, dpi):
        self.model = model
        self.color = color
        self.price = price
        self.dpi = dpi

    def action(self):
        return f'{self.model} сканирует'

class Xerox(OfficeEquipment):

    def __init__(self, model, color, price, weight):
        self.model = model
        self.color = color
        self.price = price
        self.weight = weight

    def action(self):
        return f'{self.model} копирует'

printer = Printer('Samsung', 'Red', 1000, 50)
scanner = Scanner('Canon', 'Purple', 900, 600)
xerox = Xerox('Xerox', 'Purple', 900, 600)
print(Printer.action(printer))
print(Scanner.action(scanner))
print(Xerox.action(xerox))