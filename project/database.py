from typing import List
from .team import DevelopmentTeam
from .task_manager import TaskManager


class DatabaseMock:
    _team = DevelopmentTeam()
    _task_manager = TaskManager()

    @classmethod
    def show_team(cls) -> str:
        return str(cls._team)
    
    @classmethod
    def show_tasks(cls) -> list[str]:
        return cls._task_manager.show_tasks()

    @classmethod
    def add_task(cls, task) -> None:
        cls._task_manager.add_task(task)
        
    @classmethod
    def clear_tasks(cls):
        cls._task_manager = TaskManager()
        
    @classmethod
    def add_memeber(cls, memeber) -> None:
        cls._team.add_member(memeber)
