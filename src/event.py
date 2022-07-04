from datetime import datetime


class Event:

    _when: datetime

    def __init__(self, when):
        self._when = when

    @property
    def when(self):
        return self._when
