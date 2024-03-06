from typing import List


class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        self.__tasks: List[Task] = []

    def add_task(self, title: str, description: str) -> None:
        task = Task(title, description)
        self.__tasks.append(task)

    @property
    def tasks(self) -> List[Task]:
        return self.__tasks

if __name__ == "__main__":
    # Создаем объект TaskManager
    task_manager = TaskManager()

    # Добавляем задачи
    task_manager.add_task("Задача 1", "Описание задачи 1")
    task_manager.add_task("Задача 2", "Описание задачи 2")

    # Получаем и выводим список задач
    tasks = task_manager.tasks
    for idx, task in enumerate(tasks, start=1):
        print(f"Задача {idx}: {task.title} - {task.description}")
