#!/bin/sh
### BEGIN INIT INFO
# Provides:          makalgo
# Required-Start:    $remote_fs $syslog $lighttpd
# Required-Stop:     $remote_fs $syslog $lighttpd
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start Makalgo
# Description:       Makalgo website
### END INIT INFO


PROJDIR=$(dirname $(readlink -e "$0"))
BASEDIR=$(dirname "$PROJDIR")

PROJNAME="elgassia"

ENVDIR="$BASEDIR/$PROJNAME-env"
PIDFILE="$BASEDIR/$PROJNAME.pid"
SOCKET="$BASEDIR/$PROJNAME.sock"

MANAGER="$PROJDIR/manage.py"

HOST=127.0.0.1
PORT="3034"

USER="www"

. $ENVDIR/bin/activate

case "$1" in
    start)
        start-stop-daemon --start --user "$USER" --chuid "$USER" \
                --startas "$MANAGER" --pidfile "$PIDFILE" \
                -- runfcgi host="$HOST" port="$PORT" pidfile="$PIDFILE"
    ;;
    stop)
        start-stop-daemon --stop --user "$USER" --startas "$MANAGER" \
                --pidfile "$PIDFILE"
    ;;
esac
