r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/j3b/EvDev/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "DROP Testing"

# open to the internet: 
# 4020 and 4021
# not 4020 for a test

WEBSOCKET_CLIENT_PORT = [4022]
AMP_PORT = 4026

# Required. Change to whichever outgoing Telnet port(s) 
# you are allowed to use on your host.
TELNET_PORTS = [4020]
# Optional for security. Restrict which telnet 
# interfaces we should accept. Should be set to your 
# outward-facing IP address(es). Default is ´0.0.0.0´
# which accepts all interfaces.
TELNET_INTERFACES = ['0.0.0.0']


# WEB SERVER
# Required. This is a list of tuples 
# (outgoing_port, internal_port). Only the outgoing
# port should be open to the world! 
# set outgoing port to 80 if you want to run Evennia
# as the only web server on your machine (if available).
WEBSERVER_PORTS = [(4021, 4025)]
# Optional for security. Change this to the IP your 
# server can be reached at (normally the same 
# as TELNET_INTERFACES)
WEBSERVER_INTERFACES = ['0.0.0.0']
# Optional for security. Protects against 
# man-in-the-middle attacks. Change  it to your server's 
# IP address or URL when you run a production server. 
ALLOWED_HOSTS = ['*']


# Required. Change this to the main IP address of your server.
WEBSOCKET_CLIENT_INTERFACE = '0.0.0.0'
# Optional and needed only if using a proxy or similar. Change 
# to the IP or address where the client can reach 
# your server. The ws:// part is then required. If not given, the client
# will use its host location.  
WEBSOCKET_CLIENT_URL = ""
# Required. Change to a free port for the websocket client to reach
# the server on. This will be automatically appended 
# to WEBSOCKET_CLIENT_URL by the web client.  
WEBSOCKET_CLIENT_PORT = 4022


# uncomment to lock down server
# LOCKDOWN_MODE = True


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
