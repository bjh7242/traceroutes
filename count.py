#!/usr/bin/env python
#cat trace| grep --no-group-separator -B 1 "traceroute to" | grep -v "traceroute to" | grep -vF "30  * * *" | awk '{ print $1}'

count = 0
# numhosts is the number of domains returning a definite traceroute
# the commented command on line 2 should be used to remove all traceroutes that do not fully complete (ex. if
# a host is blocking ICMP port unreachable messages)
numhosts = 0

with open('hops','r') as f:
    for num in f:
        count += int(num)
        numhosts += 1

#print count
#print numhosts
print "The average number of hops is: " + str(float(count)/float(numhosts))
