# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_stop_task_activity_400 1'] = [
    'Задача не взята в работу'
]

snapshots['test_stop_task_activity_401 1'] = {
    'detail': 'Authentication credentials were not provided.'
}
