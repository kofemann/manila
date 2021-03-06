.. -*- rst -*-

.. _get-access-rules-before-2-45:

=============
Share actions
=============

Share actions include granting or revoking share access, listing the
available access rules for a share, explicitly updating the state of a
share, resizing a share and un-managing a share.

As administrator, you can reset the state of a share and force-
delete a share in any state. Use the ``policy.json`` file to grant
permissions for this action to other roles.

You can set the state of a share to one of these supported states:

- ``available``

- ``error``

- ``creating``

- ``deleting``

- ``error_deleting``

If API version 1.0-2.6 is used then all share actions, defined
below, should include prefix ``os-`` in top element of request
JSON's body.

For example: {"access_list": null} is valid for v2.7+. And {"os-
access_list": null} is valid for v1.0-2.6


Grant access
============

All manila shares begin with no access. Clients must be provided with
explicit access via this API.

To grant access, specify one of these supported share access levels:

- ``rw``. Read and write (RW) access.

- ``ro``. Read-only (RO) access.

You must also specify one of these supported authentication
methods:

- ``ip``. Authenticates an instance through its IP address.
  The value specified should be a valid IPv4 or an IPv6 address,
  or a subnet in CIDR notation.
  A valid format is ``X:X:X:X:X:X:X:X``, ``X:X:X:X:X:X:X:X/XX``,
  ``XX.XX.XX.XX``, or ``XX.XX.XX.XX/XX``, etc. For
  example ``0.0.0.0/0`` or ``::/0``.

.. important::

  IPv6 based access is only supported with API version 2.38 and beyond.

- ``cert``. Authenticates an instance through a TLS certificate.
  Specify the TLS identity as the IDENTKEY. A valid value is any
  string up to 64 characters long in the common name (CN) of the
  certificate. The meaning of a string depends on its
  interpretation.

- ``user``. Authenticates by a user or group name. A valid value is
  an alphanumeric string that can contain some special characters
  and is from 4 to 255 characters long.

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Grants access to a share.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - allow_access: allow_access
   - access_level: access_level
   - access_type: access_type
   - access_to: access_to
   - share_id: share_id
   - tenant_id: tenant_id_path
   - access_metadata: metadata

Request example
---------------

.. literalinclude:: samples/share-actions-grant-access-request.json
   :language: javascript

Response parameters
-------------------

.. rest_parameters:: parameters.yaml

   - share_id: access_share_id
   - created_at: access_rule_created_at
   - updated_at: access_rule_updated_at
   - access_type: access_type
   - access_to: access_to
   - access_key: access_key
   - access: access
   - access_level: access_level
   - id: access_rule_id
   - access_metadata: access_metadata

Response example
----------------

.. literalinclude:: samples/share-actions-grant-access-response.json
   :language: javascript


Revoke access
=============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

The shared file systems service stores each access rule in its database and
assigns it a unique ID. This ID can be used to revoke access after access
has been requested.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - deny_access: deny_access
   - access_id: access_id
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-revoke-access-request.json
   :language: javascript


List access rules (versions 1.0 to 2.44)
========================================

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Lists access rules for a share. The Access ID returned is necessary to deny
access.

.. note::
  Use :ref:`List share access rules <get-access-rules-after-2-45>` API
  instead of this API from version 2.45

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 200

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - access_list: access_list
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-list-access-rules-request.json
   :language: javascript


Response parameters
-------------------

.. rest_parameters:: parameters.yaml

   - access_type: access_type
   - access_key: access_key
   - access_to: access_to
   - access_level: access_level
   - state: state
   - access_list: access_list
   - id: access_rule_id
   - created_at: access_rule_created_at
   - updated_at: access_rule_updated_at

Response example
----------------

.. literalinclude:: samples/share-actions-list-access-rules-response.json
   :language: javascript


Reset share state
=================

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Administrator only. Explicitly updates the state of a share.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - reset_status: reset_status
   - status: access_status
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-reset-state-request.json
   :language: javascript


Force-delete share
==================

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Administrator only. Force-deletes a share in any state.

Use the ``policy.json`` file to grant permissions for this action
to other roles.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - force_delete: share_force_delete
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-force-delete-request.json
   :language: javascript


Extend share
============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Increases the size of a share.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - extend: extend
   - new_size: share_new_size
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-extend-request.json
   :language: javascript


Shrink share
============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Shrinks the size of a share.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404

Request
-------

.. rest_parameters:: parameters.yaml

   - shrink: shrink
   - new_size: share_new_size
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-shrink-request.json
   :language: javascript


Unmanage share
==============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

This API is available in versions later than or equal to 2.7

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404
   - 409

Request
-------

.. rest_parameters:: parameters.yaml

   - unmanage: share_unmanage
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-unmanage-request.json
   :language: javascript


Revert share to snapshot
========================

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Reverts a share to the specified snapshot, which must be the most recent one
known to manila. This API is available in versions later than or equal to 2.27.

Response codes
--------------

.. rest_status_code:: success status.yaml

   - 202

.. rest_status_code:: error status.yaml

   - 400
   - 401
   - 403
   - 404
   - 409

Request
-------

.. rest_parameters:: parameters.yaml

   - snapshot_id: snapshot_id
   - share_id: share_id
   - tenant_id: tenant_id_path

Request example
---------------

.. literalinclude:: samples/share-actions-revert-to-snapshot-request.json
   :language: javascript
