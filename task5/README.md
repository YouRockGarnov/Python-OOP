Задача: Управление командой разработчиков

Вы разрабатываете программу для управления командой разработчиков, и вам нужно создать классы для разных типов разработчиков и их команд. Используйте композицию и абстрактные классы, чтобы упростить структуру вашей программы.

Создайте абстрактный класс Developer, который будет представлять общий интерфейс для всех типов разработчиков. У этого класса должны быть абстрактные методы work и get_salary.
Создайте класс BackEndDeveloper, который наследуется от Developer. Реализуйте абстрактные методы work и get_salary. Метод work должен выводить сообщение о разработке серверной части приложения.
Создайте класс FrontEndDeveloper, также наследующийся от Developer, и реализуйте абстрактные методы work и get_salary. Метод work должен выводить сообщение о разработке клиентской части приложения.
Создайте класс TeamLead, который также наследуется от Developer. Реализуйте абстрактный метод work, который выводит сообщение о координации работы команды. Реализуйте метод get_salary, который возвращает зарплату как сумму зарплат всех членов команды.
Создайте класс DevelopmentTeam, который представляет команду разработчиков. Используйте композицию, чтобы добавить в команду несколько объектов разработчиков (например, 2 BackEndDeveloper и 3 FrontEndDeveloper). Реализуйте метод work, который вызывает метод work для каждого разработчика в команде.
Создайте объекты для каждого типа разработчиков (например, back_end_dev, front_end_dev1, front_end_dev2, team_lead) и добавьте их в объект DevelopmentTeam. Вызовите метод work для команды и выведите результат.
Вызовите метод get_salary для объекта team_lead и выведите сумму зарплаты для всей команды.
Эта задача поможет студентам применить понимание композиции и абстрактных классов для создания структуры управления командой разработчиков.
