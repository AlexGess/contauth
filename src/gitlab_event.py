from event import Event


class GitlabEvent(Event):

    _username: str

    def __init__(self, when, username):
        self._username = username

    @property
    def username(self):
        return self._username   
