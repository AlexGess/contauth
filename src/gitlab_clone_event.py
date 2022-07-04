from network_event import NetworkEvent
from gitlab_event import GitlabEvent


class GitlabCloneEvent(GitlabEvent, NetworkEvent):

    _repository: str

    def __init__(self, when, remote_address, username, repository):
        GitlabEvent.__init__(self, when, username)
        NetworkEvent.__init__(self, when, remote_address)
        self._repository = repository

    @property
    def repository(self):
        return self._repository
