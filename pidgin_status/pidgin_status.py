#!/usr/bin/python
import dbus, gobject, os, sys

# Status constants
STATUS_OFFLINE = 1
STATUS_ONLINE = 2 

# Get purple DBUS object
bus    = dbus.SessionBus()
obj    = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

# Check command line arguments
method = None
if len(sys.argv) > 1:
    method = sys.argv[1]

if method not in ('--offline', '--online'):
    print 'Use either with --offline or --online'
    sys.exit(0)

# Check what to do
if method == '--offline':
    # Create the offline status and activate it
    offlineStatus = purple.PurpleSavedstatusNew("", STATUS_OFFLINE)
    purple.PurpleSavedstatusActivate(offlineStatus)

    print 'Gone offline'
else:
    try:
        # Create online status and activate it
	onlineStatus = purple.PurpleSavedstatusNew("", STATUS_ONLINE)
        purple.PurpleSavedstatusActivate(onlineStatus)

        print 'Status online'
    except:
        print 'Could not online status'
