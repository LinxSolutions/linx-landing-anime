#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/linx/landing")

from web import app as application
application.secret_key = 'linx'