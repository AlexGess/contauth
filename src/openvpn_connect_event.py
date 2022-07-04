from network_event import NetworkEvent
from openvpn_event import OpenvpnEvent


class OpenvpnConnectEvent(OpenvpnEvent, NetworkEvent):

    _username: str

    def __init__(self, when, remote_address, username):
        NetworkEvent.__init__(self, when, remote_address)
        self._username = username
