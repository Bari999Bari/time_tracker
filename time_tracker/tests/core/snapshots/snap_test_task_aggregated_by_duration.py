# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_task_aggregate_by_duration_200 1'] = [
    {
        'duration': '02:00',
        'task_name': 'first'
    }
]
