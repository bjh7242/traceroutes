#!/usr/bin/env python
#cat trace| grep --no-group-separator -B 1 "traceroute to" | grep -v "traceroute to" | grep -vF "30  * * *" | awk '{ print $1}'


