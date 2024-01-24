from typing import List


class Task:
    def __init__(self, title: str, description: str) -> None:
        raise NotImplementedError("Implement me")


class TaskManager:
    def __init__(self):
        raise NotImplementedError("Implement me")

    def add_task(self, title: str, description: str) -> None:
        raise NotImplementedError("Implement me")

    @property
    def tasks(self) -> List[Task]:
        raise NotImplementedError("Implement me")

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
