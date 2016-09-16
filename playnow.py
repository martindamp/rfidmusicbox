import subprocess
import sys

uri =  str(sys.argv[1])

cmd = 'mpc clear;mpc add '+uri+';mpc play'

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
