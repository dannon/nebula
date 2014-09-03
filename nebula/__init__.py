
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import os
import sys
import time
import argparse
import logging
import hashlib
import uuid


logging.basicConfig(level=logging.INFO)

from parser import NebulaCompile
from scheduler import Scheduler
from website import WebSite

PENDING = 'PENDING'
FAILED = 'FAILED'
DONE = 'DONE'
RUNNING = 'RUNNING'
UNKNOWN = 'UNKNOWN'




class CompileException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg


class Config:
    def __init__(self, mesos=None, port=9999):
        self.mesos = mesos
        self.port = port