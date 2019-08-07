# EVBox check script

Python script to fetch and filter NON OK services using the payload "http://hiring.test.everon.io/"

# Requirements

- python3 must be installed
- the following python modules must be installed: [requests], [argparse]:
$ pip install requests argparse

# Why Python3?
I really enjoy coding in python because it's a modern scripting language which generates a pretty clean code. I tend to prefer python3 over bash when I have a bit more time for writing the code.

# Requisites

- It must accept the address as an argument [OKAY]
- It must exist with a non zero exit code if something is wrong. [OKAY]
- It must list all the services that are not ok in the following format “The service $name is $status” [OKAY]

# Syntax

$ ./check.py [URL]

# Expected output

$ ./check.py http://hiring.test.everon.io

The following services are NOT OK:

The Service notifications is NOK

The Service roaming is down

The Service auth is degraded service
