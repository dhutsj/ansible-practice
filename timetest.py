#!/usr/bin/python

import datetime
import json
from tzlocal import get_localzone

date = str(datetime.datetime.now())
timezone = get_localzone()
timezone = timezone.__str__()

print(json.dumps({
        "time" : date,
        "timezone": timezone
        }))
