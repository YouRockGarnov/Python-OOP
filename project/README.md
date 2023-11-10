
# Задача: Разработка Диалоговой Системы с использованием State Machine

## Описание:
Вашей задачей является создание диалоговой системы с использованием паттерна проектирования [State Machine](https://refactoring.guru/design-patterns/state). Вам предоставлены два абстрактных класса - `Bot` и `State`.

### 1. `Bot` класс:
   - Абстрактный класс, содержащий метод `reply(message: str) -> None`, который принимает сообщение пользователя.
   - Ваша задача - реализовать функциональность ответа бота на различные входящие сообщения.

### 2. `State` класс:
   - Абстрактный класс, содержащий абстрактный метод `act() -> None`, который определяет действие, выполняемое ботом в данном состоянии.
   - Имеет абстрактное поле `next_state`, которое указывает на следующее состояние, в которое бот должен перейти после завершения текущего действия.

## Использование:
   - Вам предоставлены абстрактные классы `Bot` и `State`. Создайте класс, наследующийся от `Bot` и реализующий метод `reply`. Класс должен также содержать различные состояния, которые наследуются от `State`. Установите логику переходов между состояниями с использованием `next_state`.

## Пример использования:
```python
from abc import ABC, abstractmethod
from typing import Type

class Bot(ABC):
    @abstractmethod
    def reply(self, message: str) -> None:
        pass

class State(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    next_state: Type[State]  # Абстрактное поле для следующего состояния

class MyBot(Bot):
    def __init__(self, initial_state: Type[State]) -> None:
        self.current_state = initial_state(self)

class GreetingState(State):
    def act(self) -> None:
        print("Hello! How can I help you today?")
        self.bot.current_state = MainState(self.bot)

class MainState(State):
    def act(self) -> None:
        print("I'm in the main state. What would you like to do?")
        # Implement your logic here
```

## Замечание:
   - Обратите внимание, что это абстрактная задача, и вы свободны реализовать логику бота и состояний в соответствии с вашим видением. Важно обеспечить правильные переходы между состояниями и корректное выполнение действий в каждом из них.

## Цель:
   - Понимание и применение паттерна проектирования State Machine для построения гибкой и расширяемой диалоговой системы, используя абстрактные классы.
