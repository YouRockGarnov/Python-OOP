import pytest
from task_manager import TaskManager


def test_add_task() -> None:
    task_manager = TaskManager()
    task_manager.add_task("Задача 1", "Описание задачи 1")
    tasks = task_manager.tasks

    assert len(tasks) == 1
    added_task = tasks[0]
    assert added_task.title == "Задача 1"
    assert added_task.description == "Описание задачи 1"


def test_get_tasks():
    task_manager = TaskManager()
    task_manager.add_task("Задача 1", "Описание задачи 1")
    task_manager.add_task("Задача 2", "Описание задачи 2")

    tasks = task_manager.tasks
    assert len(tasks) == 2

    task1, task2 = tasks
    assert task1.title == "Задача 1"
    assert task1.description == "Описание задачи 1"
    assert task2.title == "Задача 2"
    assert task2.description == "Описание задачи 2"


if __name__ == "__main__":
    pytest.main([__file__])
