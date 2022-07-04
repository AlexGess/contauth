from typing import List
from typing import Dict
from typing import TypeVar
from typing import Generic
import yaml

from gitlab_log_parser import LogParser
from gitlab_log_parser import GitlabLogParser
from gitlab_clone_event import GitlabCloneEvent
from openvpn_connect_event import OpenvpnConnectEvent

T = TypeVar('T')


class ContAuthApp:

    _config: Dict[str, T]
    _parsers: List[LogParser] = []

    def run(self, argv):
        config_filename = self._get_config_filename_from_argv(argv)
        self._config = self._read_config(config_filename)
        self._add_parsers()
        self._routine()

    def _add_parsers(self):
        self._parsers.append(GitlabLogParser(self._config['logs']['gitlab']))
        # ...

    def _get_config_filename_from_argv(self, argv):
        try:
            config_filename = argv[1]
            return config_filename
        except IndexError:
            raise RuntimeError('Missing config filename')

    def _read_config(self, config_filename):
        with open(config_filename, 'r') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            return data

    def _routine(self):
        while True:
            for parser in self._parsers:
                self._process_parser(parser)

    def _process_parser(self, parser):
        event = parser.next_event()
        if event:
            print(event.when)
