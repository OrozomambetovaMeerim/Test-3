# Дайте определение термину "итератор"? Опрелеления (txt формат) и код  (.py) залейте на гит хаб, прикркпите ссылку (можете прикрепить общую ссылку со всеми заданиями)

# Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз.

# С точки зрения Python - это любой объект, у которого есть метод __next__. Этот метод возвращает следующий элемент, если он есть, или возвращает исключение StopIteration, когда элементы закончились.

class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))