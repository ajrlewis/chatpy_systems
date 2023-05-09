import abc
from typing import List
import chatpy as cp


class System(abc.ABC):
    def __init__(self, chat: cp.Chat) -> str:
        self._chat = chat
        if self._chat.system != self.system:
            self._chat.system = self.system

    def __str__(self):
        return f"{self._chat}"

    @property
    @abc.abstractmethod
    def system(self) -> str:
        ...

    def ask(self, question: str) -> str:
        return self._chat.ask(question=question)
