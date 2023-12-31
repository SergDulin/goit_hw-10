# Домашнє завдання

GOIT > Курс > Python Developer > Python core > Модуль 10. Основи роботи з класами

# Додаток Телефонна книга

У цій роботі ми продовжили розвивати нашого віртуального асистента з CLI інтерфейсом.

https://github.com/SergDulin/goit_hw-09/blob/main/goit_hw-09.py - посилання на попереднє завдання.

Наш асистент вміє взаємодіяти з користувачем за допомогою командного рядка, отримуючи команди та аргументи, та виконуючи потрібні дії. У цьому завданні ми попрацювали над внутрішньою логікою асистента, над тим, як зберігаються дані, які саме дані і що з ними можна зробити.Для цих цілей ми застосували об'єктно-орієнтоване програмування.

## Використання

Додаток підтримує наступні команди:

- `hello`: Виводить привітальне повідомлення.
- `add [name] [phone]`: Додає контакт з вказаним іменем та номером телефону.
- `change [name] [phone]`: Змінює номер телефону існуючого контакту з вказаним іменем.
- `phone [name]`: Отримує номер телефону контакту за іменем.
- `show all`: Відображає всі контакти в телефонній книзі.
- `good`, `bye`, `close`, `exit`: Виходить з додатку.

## Опис роботи

Цей код реалізує простий зберігач контактів з можливістю додавання, зміни та отримання номерів телефонів контактів, а також виведення всіх контактів. Він також має базовий інтерфейс командного рядка для взаємодії з користувачем.

Ім'я контакту може бути с декілька слів, необхідно мінімум одно. При пошуку чи зміні телефону, можливо вводити ім'я любим регістром. Команда "show all" виводить імена з великої літери. При пошуку телефону достатньо одного імені, команда "phone" виводить список телефонов в яких є таке ім'я.

## Особливості роботи

Клас AddressBook, який унаслідується від UserDict, та відповідає за логіку пошуку за записами до цього класу та клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.

Записи Record в AddressBook зберігаються як значення у словнику. Як ключі використовується значення Record.name.value.
Record зберігає об'єкт Name та список об'єктів Phone в окремому атрибуті.
Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
AddressBook реалізує метод add_record, який додає Record у self.data.
