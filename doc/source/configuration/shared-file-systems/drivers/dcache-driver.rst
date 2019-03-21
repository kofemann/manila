========================
dCache NFS server driver
========================

The Shared File Systems driver for dCache is a distributed storage system that
used to store experimental data by many scientific communities.

Supported shared filesystems and operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The driver supports NFS shares only.

The following operations are supported:

- Create a share.

- Delete a share.

- Allow share access.

  Note the following limitations:

  - Only IP access type is supported for NFS.

- Deny share access.

- Extend a share.

- Shrink a share.

Requirements
------------

 - dCache running NFS service

 - The following export file and directories are used:

  - ``/etc/dcache/exports``

  - ``/etc/dcache/exports.d``

Driver options
~~~~~~~~~~~~~~

The following table contains the configuration options specific to this
driver.

.. include:: ../../tables/manila-dcache.inc