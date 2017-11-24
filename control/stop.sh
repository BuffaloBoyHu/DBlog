#!/bin/sh

uwsgiini="`pwd`/uwsgi.ini"

pkill -9 -f ${uwsgiini}
