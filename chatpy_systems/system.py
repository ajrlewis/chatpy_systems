from typing import List
import chatpy as cp


class System:
    def __init__(
        self, who_the_system_is: str, what_the_system_will_do: str, chat: cp.Chat
    ) -> str:
        self.who_the_system_is = who_the_system_is
        self.what_the_system_will_do = what_the_system_will_do
        self._chat = chat
        system = self.get_system()
        if self._chat.system != system:
            self._chat.system = system

    def __str__(self):
        return f"{self._chat}"

    def get_system(self):
        return f"""
Please forget all prior prompts.
{self.who_the_system_is}
Under no circumstances should you ever break character.

{self.what_the_system_will_do}

You are doing great and continue to do better each time.
Let's go, and please enjoy!
Thank you.
        """

    def ask(self, question: str) -> str:
        return self._chat.ask(question=question)
