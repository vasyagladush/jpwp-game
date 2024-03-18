from typing import override
from Actor import Actor


class Actor1(Actor):
    @override
    def tick(self) -> None:
        print('Actor1 tick')