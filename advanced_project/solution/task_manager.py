from typing import List


class Task:
    def __init__(self, title: str) -> None:
        self.title = title


class TaskManager:
    def __init__(self):
        self.__tasks: List[Task] = []

    def add_task(self, title: str) -> None:
        task = Task(title)
        self.__tasks.append(task)

    @property
    def tasks(self) -> List[Task]:
        return self.__tasks
    
    def show_tasks(self) -> list[str]:
        return [task.title for task in self.__tasks]
