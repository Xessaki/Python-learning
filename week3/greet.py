def greet (name, age):
    print(f'Привет, {name}! Тебе {age} лет.')

name = input('Как тебя зовут?')
age = int(input('Сколько тебе лет?'))

greet(name, age)