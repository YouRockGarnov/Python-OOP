from typing import Dict
from .team import BackEndDeveloper, FrontEndDeveloper, TeamLead
from .database import DatabaseMock
from ..commands import Commands
import abc


class StateBase(abc.ABC):
    @abc.abstractmethod
    def act(self, message: str) -> str:
        pass
    
    @abc.abstractmethod
    def make_next_state(self) -> object:
        pass
        
        
class MainState(StateBase):
    def __init__(self) -> None:
        self._next_state = self
    
    def act(self, message: str) -> str:
        if message in self.command_to_action and message in self.command_to_state:
            self._next_state = self.command_to_state[message]()
            return self.command_to_action[message]()
    
    def make_next_state(self):
        return self._next_state
           
    @property
    def command_to_state(self):
        return {
            Commands.add_task._value_: AddTaskState,
            Commands.show_tasks._value_: MainState,
            Commands.add_developer._value_: AddDeveloperState,
            Commands.show_team._value_: MainState,
            Commands.pay_salary._value_: MainState,
        }
        
    @property
    def command_to_action(self):
        return {
            Commands.add_task._value_: lambda: 'Какое у нее название?',
            Commands.show_tasks._value_: self._show_tasks,
            Commands.add_developer._value_: lambda: 'Какого? Frontend, Backend или TeamLead?',
            Commands.show_team._value_: self._show_team,
            Commands.pay_salary._value_: self._pay_salary,
        }
    
    @classmethod
    def _show_tasks(cls) -> str:
        return str(DatabaseMock.show_tasks())
    
    @classmethod
    def _show_team(cls) -> str:
        return str(DatabaseMock.show_team())
    
    @classmethod
    def _pay_salary(cls) -> str:
        DatabaseMock.pay_salary()
        return 'Зарплата успешно начислена!'
            
            
class AddTaskState(StateBase):
    def act(self, message: str) -> str:
        DatabaseMock.add_task(message)
    
    def make_next_state(self) -> MainState:
        return MainState()


class AddDeveloperState(StateBase):        
    def act(self, message: str) -> str:
        if message in self.message_to_developer:
            self._next_state = MainState()
            DatabaseMock.add_memeber(self.message_to_developer[message]())
            return 'Добавил нового разработчика.'
        else:
            self._next_state = self
            
    def make_next_state(self) -> MainState:
        return MainState()
    
    @property
    def message_to_developer(self) -> Dict:
        return {
            Commands.backend.value: BackEndDeveloper,
            Commands.frontend.value: FrontEndDeveloper,
            Commands.teamlead.value: TeamLead,
        }


class StartState(StateBase):
    def act(self, message: str) -> str:
        return 'Здравствуйте!'
    
    def make_next_state(self) -> MainState:
        return MainState()
