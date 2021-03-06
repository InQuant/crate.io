#  -*- coding: utf-8 -*-
#
#  File Name: fix_missing_files.py
#  Creation Date: 2012 Jul 24
#  Last Modified: 2013 Mai 02

#  Copyright (c) 2003-2012 InQuant GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


__author__ = 'Daniel Altiparmak <daniel.altiparmak@inquant.de>'
__docformat__ = 'plaintext'

from django.core.management.base import BaseCommand

from crate.web.packages.models import ReleaseFile
from crate.pypi.processor import PyPIPackage
from crate.pypi.tasks import bulk_synchronize

class Command(BaseCommand):

    def handle(self, *args, **options):
        async_result = bulk_synchronize.delay()
        print "AsyncResult %s created" % async_result


# vim: set ft=python ts=4 sw=4 expandtab :

