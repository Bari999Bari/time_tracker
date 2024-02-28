# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_task_activities_200 1'] = [
    {
        'finished_at': '2024-02-23 12:30',
        'started_at': '2024-02-23 10:30',
        'task': 201
    }
]
