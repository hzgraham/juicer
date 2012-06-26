import os
import sys

from distutils.core import setup

setup(name='juicer',
      version='0.1.0',
      description='Administer Pulp and Release Carts',
      author='GCA-PC',
      author_email='it-pc-list@redhat.com',
      url='https://docspace.corp.redhat.com/docs/DOC-104668',
      license='GPLv3+',
      package_dir={ 'juicer': 'juicer' },
      packages=[
         'juicer',
         'juicer.juicer',
         'juicer.admin',
         'juicer.common',
         'juicer.utils',
      ],
      scripts=[
         'bin/juicer',
         'bin/juicer-admin'
      ]
)
