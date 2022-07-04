from abc import abstractmethod
from typing import Optional

from event import Event


class LogParser:

    @abstractmethod
    def next_event(self) -> Optional[Event]:
        pass
