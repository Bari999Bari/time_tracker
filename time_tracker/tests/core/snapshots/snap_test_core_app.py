# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_start_task_activity_400 1'] = [
    'Данная задача уже в работе'
]

snapshots['test_start_task_activity_401 1'] = {
    'detail': 'Authentication credentials were not provided.'
}
