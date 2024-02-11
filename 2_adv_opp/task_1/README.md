Домашнее задание: Изучение разных типов методов в Python
Описание:

В этом задании вы будете изучать различные типы методов в Python и их применение. Вы создадите класс с использованием обычных методов экземпляра, статических методов, методов класса, специальных методов (магических методов) и property методов. Затем вы протестируете ваш класс, чтобы убедиться, что все методы работают правильно.

Упражнения:

Создайте класс MyClass.
Добавьте атрибут класса class_attribute, равный строке "I am a class attribute".
Реализуйте конструктор __init__, который принимает аргумент instance_attribute и устанавливает его как атрибут экземпляра.
Создайте обычный метод экземпляра instance_method, который возвращает строку "I am an instance method, my instance attribute is [значение instance_attribute]".
Определите статический метод static_method, который возвращает строку "I am a static method, I don't need access to instance or class attributes".
Реализуйте метод класса class_method, который возвращает строку "I am a class method, my class attribute is [значение class_attribute]".
Переопределите специальный метод __str__, чтобы он возвращал строку "MyClass instance with instance attribute: [значение instance_attribute]".
Создайте property метод instance_attribute_squared, который возвращает квадрат значения атрибута instance_attribute.
Дополнительные материалы:

Официальная документация Python по классам и методам
