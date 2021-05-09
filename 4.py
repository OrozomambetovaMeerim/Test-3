# Дайте определение термину "абстракция". Опрелеления (txt формат) и код  (.py) залейте на гит хаб, прикркпите ссылку (можете прикрепить общую ссылку со всеми заданиями)

# Абстрактным называется класс, который содержит один и более абстрактных методов. Абстрактным называется объявленный, но не реализованный метод. Абстрактные классы не могут быть инстанциированы, от них нужно унаследовать, реализовать все их абстрактные методы и только тогда можно создать экземпляр такого класса. В Python отсутствует встроенная поддержка абстрактных классов, для этой цели используется модуль abc (Abstract Base Class)

from abc import ABC, abstractmethod
 
class ChessPiece(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def draw(self):
        print("Drew a chess piece")
 
    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def move(self):
        pass


class Queen(ChessPiece):
    def move(self):
        print("Moved Queen to e2e4")
 
# Мы можем создать экземпляр класса
q = Queen()
# И нам доступны все методы класса
q.draw()
q.move()



from abc import ABC, abstractmethod
 
 
class Basic(ABC):
    @abstractmethod
    def hello(self):
        print("Hello from Basic class")
 
 
class Advanced(Basic):
    def hello(self):
        super().hello()
        print("Enriched functionality")
 
a = Advanced()
a.hello()