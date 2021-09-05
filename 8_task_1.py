# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def transform(self, dmy):
        date = []
        for i in dmy.split():
            if i != '-':
                date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def check(dmy):
        date_2 = []
        for i in dmy.split('-'):
            if i != '-':
                date_2.append(i)
                if 1 <= int(date_2[0]) <= 31:
                    if 1 <= int(date_2[1]) <= 12: # не удалось исправить ошибку((
                        if 0 <= int(date_2[2]):
                            return f'Дата введена верно!'
                        else:
                            return f'Год введён некорректно, укажите год не меньше 0'
                    else:
                        return f'Месяц введён некорректно, укажите месяц от 1 до 12'
                else:
                    return f'День введён некорректно, укажите день от 1 до 31'
                # for date_2[0] in date_2:
                #     if 1 <= int(date_2[0]) <= 31:
                #         print(f'День введён верно!')
                #     else:
                #         return f'День введён некорректно, укажите день от 1 до 31'
                # for date_2[1] in date_2:
                #     if 1 <= int(date_2[1]) <= 12:
                #         return f'Месяц введён верно!'
                #     else:
                #         return f'Месяц введён некорректно, укажите месяц от 1 до 12'
                # for date_2[0] in date_2:
                #     if 0 <= int(date_2[2]):
                #        return f'Год введён верно!'
                #     else:
                #        return f'Год введён некорректно, укажите год не меньше 0'







print(Date.transform('31 - 07 - 1992'))
print(Date.check('31 - 7 - 1993'))
print(Date.check('32 - 15 - 2000'))