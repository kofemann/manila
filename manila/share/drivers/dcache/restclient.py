# Copyright (c) 2019 Deutsches Elektronen-Synchroton DESY.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import requests
from requests import codes

from oslo_log import log
from manila import exception

LOG = log.getLogger(__name__)
session = requests.Session()

WS_PATH="/v1/exports"

class DCacheRestClient(object):

    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.base_url = endpoint + WS_PATH

    def create_share(self, path):
        result = requests.post(
            url = self.base_url + '/' + path
        )

        if result.status_code != codes['CREATED']:
            LOG.debug("dCache REST-API error: %s", result.text)
            raise exception.DCacheException(msg=result.text)

    def delete_share(self, path):
        result = requests.delete(
            url = self.base_url + '/' + path
        )

        if result.status_code != codes['OK']:
            LOG.debug("dCache REST-API error: %s", result.text)
            raise exception.DCacheException(msg=result.text)

    def update_access(self, path, rule, ip, iomode):
        access_data = {
            "client" : ip,
            "iomode" : iomode,
            "rule" : rule
        }

        result = requests.put(
            url = self.base_url + '/' + path,
            json=access_data
        )

        if result.status_code != codes['OK']:
            LOG.debug("dCache REST-API error: %s", result.text)
            raise exception.DCacheException(msg=result.text)
