# Абстрактным называется класс, который содержит один и более абстрактных методов. 

# Композиция : Она позволяет обрабатывать группу объектов так же, как и один экземпляр объекта. Цель композита состоит в том, чтобы объединить объекты в древовидные структуры для представления иерархий "часть-целое ".


# Наследование: класс наследует поля и методы от всех своих суперклассов, прямых или косвенных. 

class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square
 
r1 = Room(6, 3, 2.7) 
print(r1.square) # выведет 48.6
r1.addWD(1, 1) 
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.workSurface()) # выведет 44.6