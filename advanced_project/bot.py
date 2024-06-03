from .solution.states import StartState


class Bot:
    def __init__(self) -> None:
        self._current_state = StartState()
    
    def reply(self, message: str) -> str:
        reply = self._current_state.act(message)
        self._current_state = self._current_state.make_next_state()
        return reply
