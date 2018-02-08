import subprocess
p = subprocess.Popen(["/usr/local/bin/yowsup-cli", "demos", "-c", "/home/matthieu/dusche/yowsup/config", "-s", "49XXXXXXXXXX", "'Das ist ein Test'"], stdout=subprocess.PIPE)
output, err = p.communicate()
