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

"""
:mod:`dcache.options` -- Contains configuration options for dCache drivers
=============================================================================

.. automodule:: dcache.options
"""

from oslo_config import cfg

dcache_connection_opts = [
    cfg.StrOpt('dcache_api_url',
               help='URL of dCache REST API endpoint.'),
    cfg.StrOpt('dcache_admin_user',
               default='admin',
               help='User name to connect to dCache.'),
    cfg.StrOpt('dcache_admin_password',
               help='Password to connect to dCache.',
               secret=True),
    cfg.FloatOpt('dcache_rest_connect_timeout',
                default=30,
                help='Specifies the time limit (in seconds), within '
                      'which the connection to dCache management '
                      'REST API server must be established'),
    cfg.FloatOpt('dcache_rest_read_timeout',
                default=300,
                help='Specifies the time limit (in seconds), '
                      'within which dCache management '
                      'REST API server must send a response'),
]

dcache_nfs_opts = [
    cfg.StrOpt('dcache_door',
               help='IP address of dCache NFS door.'),
]

dcache_dataset_opts = [
]
