from ipaddress import ip_address

from event import Event


class NetworkEvent(Event):

    _remote_address: ip_address

    def __init__(self, when, remote_address):
        Event.__init__(self, when)
        self._remote_address = remote_address

    @property
    def remote_address(self):
        return self._remote_address
