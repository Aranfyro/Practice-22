# Домашняя работа по уроку "Пространство имен."

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function() # Вызов данной функции инициирует вызов внутренней функции и печатается значение

inner_function() # Вызывается внутренняя функция вне её области видимости и завершается ошибкой

