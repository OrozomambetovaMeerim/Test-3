# Что такое "генератор"? В чем его главное отличие от классических итераторов? 

# Генератор — это итератор, который работает в режиме обработки по необходимости.
# Доступно два способа создания generator: выражение генератора и функция генератора.
# Выражение-генератор похож на преобразование списка, за исключением детали (). Раз generator является итератором, мы пользуемся функцией next, чтобы получить следующий элемент.
g1 = (x*x for x in range(10))
print(type(g1))
print(next(g1))
print(next(g1))# <type 'generator'>
# 0
# 1
# Разница тут в том, что мы не вычисляем все значения при создании generator. x*x вычисляется тогда, когда мы итерируем generator.