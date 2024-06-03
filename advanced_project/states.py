import abc


class StateBase(abc.ABC):
    @abc.abstractmethod
    def act(message: str) -> str:
        pass


class MainState(StateBase):
    def __init__(self) -> None:
        self._next_state = self


class StartState(StateBase):
    def act(self, message: str) -> str:
        return 'Здравствуйте!'
    
    def make_next_state(self) -> MainState:
        return MainState()
