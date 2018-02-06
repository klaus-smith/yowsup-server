#!/usr/bin/env python

print "Content-type: text/html"
print
print "<html><head><title>Situation snapshot</title></head>"
print "<body><pre>"

import subprocess
import sys
sys.stderr = sys.stdout
import os
from cgi import escape

#p = subprocess.Popen(["/usr/local/bin/yowsup-cli", "demos", "-c", "/home/matthieu/dusche/yowsup/config", "-s", "491727393523", "'Das ist ein Test'"], stdout=subprocess.PIPE)

#output, err = p.communicate()

#os.system("python dusche.py")

print "<strong>Python %s</strong>" % sys.version

for k in sorted(os.environ.keys()):
        print "%s\t%s" % (escape(k), escape(os.environ[k]))

print "</pre></body></html>"
