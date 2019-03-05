# Copyright 2016 Mirantis, Inc.
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
"""Some useful fakes."""

from manila.tests.db import fakes as db_fakes

FAKE_VSCTL_LIST_INTERFACES_X = (
    'fake stuff\n'
    'foo not_a_veth something_fake bar\n'
    'foo veth11b2c34 something_fake bar\n'
    'foo veth25f6g7h manila-container="fake1" bar\n'
    'foo veth3jd83j7 manila-container="my_container" bar\n'
    'foo veth4i9j10k manila-container="fake2" bar\n'
    'more fake stuff\n'
)

FAKE_VSCTL_LIST_INTERFACES = (
    'fake stuff\n'
    'foo not_a_veth something_fake bar\n'
    'foo veth11b2c34 something_fake bar\n'
    'foo veth25f6g7h manila-container="fake1" bar\n'
    'foo veth3jd83j7 manila-container="manila_my_container" bar\n'
    'foo veth4i9j10k manila-container="fake2" bar\n'
    'more fake stuff\n'
)

FAKE_VSCTL_LIST_INTERFACE_1 = (
    'fake stuff\n'
    'foo veth11b2c34 something_fake bar\n'
    'more fake stuff\n'
)

FAKE_VSCTL_LIST_INTERFACE_2 = (
    'fake stuff\n'
    'foo veth25f6g7h manila-container="fake1" bar\n'
    'more fake stuff\n'
)

FAKE_VSCTL_LIST_INTERFACE_3_X = (
    'fake stuff\n'
    'foo veth3jd83j7 manila-container="my_container" bar\n'
    'more fake stuff\n'
)

FAKE_VSCTL_LIST_INTERFACE_3 = (
    'fake stuff\n'
    'foo veth3jd83j7 manila-container="manila_my_container" bar\n'
    'more fake stuff\n'
)

FAKE_VSCTL_LIST_INTERFACE_4 = (
    'fake stuff\n'
    'foo veth4i9j10k manila-container="fake2" bar\n'
    'more fake stuff\n'
)


def fake_share(**kwargs):
    share = {
        'id': 'fakeid',
        'share_id': 'fakeshareid',
        'name': 'fakename',
        'size': 1,
        'share_proto': 'NFS',
        'export_location': '127.0.0.1:/mnt/nfs/volume-00002',
    }
    share.update(kwargs)
    return db_fakes.FakeModel(share)


def fake_access(**kwargs):
    access = {
        'id': 'fakeaccid',
        'access_type': 'ip',
        'access_to': '10.0.0.2',
        'access_level': 'rw',
        'state': 'active',
    }
    access.update(kwargs)
    return db_fakes.FakeModel(access)


def fake_network(**kwargs):
    allocations = db_fakes.FakeModel({'id': 'fake_allocation_id',
                                      'ip_address': '127.0.0.0.1',
                                      'mac_address': 'fe:16:3e:61:e0:58'})
    network = {
        'id': 'fake_network_id',
        'server_id': 'fake_server_id',
        'network_allocations': [allocations],
        'neutron_net_id': 'fake_net',
        'neutron_subnet_id': 'fake_subnet',
    }
    network.update(kwargs)
    return db_fakes.FakeModel(network)


def fake_share_server(**kwargs):
    share_server = {
        'id': 'fake'
    }
    share_server.update(kwargs)
    return db_fakes.FakeModel(share_server)


def fake_identifier():
    return '7cf7c200-d3af-4e05-b87e-9167c95dfcad'


def fake_share_no_export_location(**kwargs):
    share = {
        'share_id': 'fakeshareid',
    }
    share.update(kwargs)
    return db_fakes.FakeModel(share)
