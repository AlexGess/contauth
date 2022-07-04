import json
from datetime import datetime
from ipaddress import ip_address
from typing import Optional

from log_parser import LogParser
from event import Event
from gitlab_event import GitlabEvent
from gitlab_clone_event import GitlabCloneEvent


class GitlabLogParser(LogParser):

    def __init__(self, filename):

        self._file = open(filename, 'r')

    def next_event(self) -> Optional[Event]:

        line = self._file.readline().rstrip()

        if line == '':
            return None

        rec = json.loads(line)

        try:
            if rec['command'] != 'git-receive-pack':
                return None

            when = datetime.strptime(rec['time'], '%Y-%m-%dT%H:%M:%SZ')
            remote_address = ip_address(rec['remote_ip'])
            username = rec['username']
            repository = rec['gl_repository']

        except Exception as e:
            return None

        return GitlabCloneEvent(when, remote_address, username, repository)

    def dispose(self):

        self._file.close()


        # {
        #  "command":"git-receive-pack",
        #  "correlation_id":"01G3BW43CP3TXKS5TKVSH1QZKD",
        #  "git_protocol":"",
        #  "gl_key_id":1,
        #  "gl_key_type":"key",
        #  "gl_project_path":"user/test",
        #  "gl_repository":"project-203",
        #  "level":"info",
        #  "msg":"executing git command",
        #  "remote_ip":"16.150.44.212",
        #  "time":"2022-05-18T15:21:00Z",
        #  "user_id":"user-2",
        #  "username":"user"
        # }