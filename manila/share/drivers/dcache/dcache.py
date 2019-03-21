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

from oslo_log import log

from manila.common import constants as common
from manila import exception
from manila.i18n import _
from manila.share import driver
from manila.share.drivers.dcache import options
from manila.share.drivers.dcache.restclient import DCacheRestClient

LOG = log.getLogger(__name__)
DRIVER_VERSION = '0.0.1'

class DCacheShareDriver(driver.ShareDriver):
    """dCache Share Driver."""

    def __init__(self, *args, **kwargs):
        """Do initialization."""
        LOG.debug('Initializing dCache driver.')
        super(DCacheShareDriver, self).__init__(False, *args, **kwargs)
        self.configuration = kwargs.get('configuration')
        if self.configuration:
            self.configuration.append_config_values(
                options.dcache_connection_opts)
            self.configuration.append_config_values(
                options.dcache_nfs_opts)
            self.configuration.append_config_values(
                options.dcache_dataset_opts)
        else:
            raise exception.BadConfigurationException(
                reason=_('dCache configuration missing.'))

        required_params = ['dcache_api_url', 'dcache_admin_user', 'dcache_admin_password', 'dcache_door']
        for param in required_params:
            if not getattr(self.configuration, '%s' % param):
                msg = 'Required parameter %s is not provided.' % param
                raise exception.DCacheException(msg)

        self.backend_name = self.configuration.safe_get('share_backend_name')
        self.rest_uri = self.configuration.safe_get('dcache_api_url')
        self.admin_user = self.configuration.safe_get('dcache_admin_user')
        self.admin_password = self.configuration.safe_get('dcache_admin_password')
        self.door = self.configuration.safe_get('dcache_door')
        self.restclient = DCacheRestClient(
            self.rest_uri,
            self.admin_user,
            self.admin_password
        )

    def ensure_share(self, context, share, share_server=None):
        """Ensure that share exists and exported."""
        LOG.debug('Ensure share: %s.', share['name'])

    def create_share(self, context, share, share_server=None):
        """Create a share."""
        path = share['name']
        LOG.debug('Creating share: %s.', path)
        self.restclient.create_share(path)
        location = {
                'path': '{}:/{}'.format(self.door, path),
        }
        return [location]

    def delete_share(self, context, share, share_server=None):
        """Delete a share."""
        path = share['name']
        LOG.info('Delete share: %s' % path)
        self.restclient.delete_share(path)

    def update_access(self, context, share, access_rules, add_rules,
                      delete_rules, share_server=None):
        """Update access rules for given share."""

        LOG.debug('Updating access to share %(id)s with following access '
                  'rules: %(rules)s', {
                      'id': share['name'],
                      'rules': [(rule.access_type, rule.access_level,
                                 rule.access_to) for rule in access_rules]})

        path = share['name']
        for rule in  add_rules:
            if rule['access_type'].lower() != 'ip':
                msg = _("Only IP access type is supported.")
                raise exception.InvalidShareAccess(reason=msg)

            self.restclient.update_access(path, "add",
                rule['access_to'], rule['access_level'])

        for rule in  delete_rules:
            if rule['access_type'].lower() != 'ip':
                msg = _("Only IP access type is supported.")
                raise exception.InvalidShareAccess(reason=msg)

            self.restclient.update_access(path, "delete",
                rule['access_to'], rule['access_level'])

    def get_network_allocations_number(self):
        """Returns number of network allocations for creating VIFs.

        Drivers that use Nova for share servers should return zero (0) here
        same as Generic driver does.
        Because Nova will handle network resources allocation.
        Drivers that handle networking itself should calculate it according
        to their own requirements. It can have 1+ network interfaces.
        """
        return 0

    def _update_share_stats(self):
        total_gb, free_gb = 1000000, 1000000

        data = dict(
            storage_protocol='NFS',
            vendor_name='dCache.ORG',
            share_backend_name=self.backend_name,
            driver_version=DRIVER_VERSION,
            total_capacity_gb=total_gb,
            free_capacity_gb=free_gb,
            reserved_percentage=self.configuration.reserved_share_percentage)
        super(DCacheShareDriver, self)._update_share_stats(data)
