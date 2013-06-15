#!/usr/bin/env python

from distutils.core import setup

setup(name='nas-power-manager',
      version='0.1',
      description=('Power manager for NAS systems.'),
      author='Jakub Matys',
      author_email='matys.jakub@gmail.com',
      url='https://github.com/jakm/nas-power-manager',
      scripts=['nas-power-manager'],
      data_files=[('/etc', ['nas-power-manager.ini']),
                  ('/usr/lib/systemd/system', ['nas-power-manager.service'])]
)
