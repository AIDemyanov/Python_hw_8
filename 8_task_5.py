# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

class Storage:
    pass

class OfficeEquipment:

    def __init__(self, model, color, price, *args):
        self.model = model
        self.color = color
        self.price = price
        self.store = []
        self.all_store = []
        self.info = {'Модель': self.model, 'Цвет': self.color, 'Цена': self.price}


    def reception(self):
        model_input = input('Введите наименование модели - ')
        color_input = input('Введите цвет товара - ')
        price_input = input('Введите цену за единицу товара в рублях - ')
        product = {'Модель': model_input, 'Цвет': color_input, 'Цена': price_input}
        self.store.append(self.info)
        self.info.update(product)
        print(f'Товаров {self.info} добавлен на склад')
        continuation = input(f'Для выхода введите "exit", чтобы продолжить добавления товаров нажмите enter - ')
        if continuation == 'exit':
            self.all_store.append(self.store)
            print(f'Список всего товара на складе: \n{self.all_store}\n')
            print(f'Программа закончена!!!')
        else:
            return OfficeEquipment.reception(self)

class Printer(OfficeEquipment):

    def __init__(self, model, color, price, speed_print, *args):
        self.model = model
        self.color = color
        self.price = price
        self.speed_print = speed_print
        self.store = []
        self.all_store = []
        self.info = {'Модель': self.model, 'Цвет': self.color, 'Цена': self.price}

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

printer = Printer('Samsung', 'Красный', 2000, 100)
scanner = Scanner('Canon', 'Фиолетовый', 1500, 600)
xerox = Xerox('Xerox', 'Розовый', 5000, 600)
print(Printer.action(printer))
print(Scanner.action(scanner))
print(Xerox.action(xerox))
print(printer.reception())