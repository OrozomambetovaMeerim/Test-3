# ак создать экземпляр класса (объект)? Напишите код. Опрелеления 

# Определение класса
# Для определения класса используется оператор class:

class имя_класса(надкласс1, надкласс2, ...):
    # определения атрибутов и методов класса
# У класса могут быть базовые (родительские) классы (надклассы), которые, если они есть, указываются в скобках после имени определяемого класса.

# Минимально возможное определение класса выглядит так:

class A:
    pass
# В терминологии Python члены класса называются атрибутами, функции класса — методами, а поля класса — свойствами (или просто атрибутами).

# Определения методов аналогичны определениям функций, но (за некоторыми исключениями, о которых ниже) методы всегда имеют первый аргумент, называемый по общепринятому соглашению self:

class A:
    def m1(self, x):
        # блок кода метода
# Определения атрибутов — обычные операторы присваивания, которые связывают некоторые значения с именами атрибутов.

class A:
    attr1 = 2 * 2
# В языке Python класс не является чем-то статическим, поэтому добавить атрибуты можно и после определения:

class A:
    pass

def my_method(self, x):
    return x * x

A.m1 = my_method
A.attr1 = 2 * 2
# Создание экземпляра
# Для создания объекта — экземпляра класса (то есть, инстанцирования класса), достаточно вызвать класс по имени и задать параметры конструктора:

class Point:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

    def __repr__(self):
        return "Point(%s, %s, %s)" % self.coord
>>> p = Point(0.0, 1.0, 0.0)
>>> p
Point(0.0, 1.0, 0.0)