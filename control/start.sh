#!/bin/sh

uwsgiini="`pwd`/uwsgi.ini"
touchfile="`pwd`/control/touch_reload_uwsgi"
touchlogfile="`pwd`/control/touch_reopen_log"
UWSGI_PATH="/home/panda/workplace/env/bin/uwsgi"

${UWSGI_PATH} --uid panda -x ${uwsgiini} --touch-reload=${touchfile} --touch-logreopen=${touchlogfile} --req-logger=file:/var/log/uwsgi/uwsgi_req.log --logger=file:/var/log/uwsgi/uwsgi_error.log

