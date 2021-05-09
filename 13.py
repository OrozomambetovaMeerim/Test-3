# Правильно ли написан код. Если нет, то какие допущены ошибки?

class Monster:

    def __init__(self, name, height, weight):

        self.name = name

        self._height = height

        self.__weight = weight

 

m = Monster('Chucky', 55, 5)

print(m.name, m._heighl, m.__weight)


# неверно написано название атрибута height


# нельзя называть атрибуты с подчеркиванием


# нельзя получить доступ к атрибутам с двойным подчеркиванием. m.__weight нужно заменить на m._Monster__weight


# нельзя передавать несколько аргументов в функцию print