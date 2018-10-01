#!/usr/bin/env python
import socket
import subprocess
import sys
from optparse import OptionParser
from datetime import datetime

if __name__ == "__main__":
    # Get options
    parser = OptionParser()
    parser.add_option("--host", help="host name", dest="host", type="string", default="127.0.0.1")
    parser.add_option("--from", help="minimum port", dest="min_port", type="int", default=1)
    parser.add_option("--to", help="maximum port", dest="max_port", type="int", default=1025)

    (options, args) = parser.parse_args()

    remoteServerIP  = socket.gethostbyname(options.host)

    # Print a nice banner with information on which host we are about to scan
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "from port {} to {}".format(options.min_port, options.max_port)
    print "-" * 60

    # Check what time the scan started
    t1 = datetime.now()

    # We also put in some error handling for catching errors
    try:
        for port in range(options.min_port, options.max_port+1):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print 'Scanning Completed in: ', total
