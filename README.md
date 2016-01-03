The first script that should be run is traceroute.sh. This script will read in the Alexa top 500 list (top500) and run a traceroute to each domain in that file. It will then write the results of each traceroute to a file (trace). 

Next, the command commented out in the count.py script should be run. This command will remove all traceroutes to domains that did not complete correctly (for example, if ICMP port unreachable messages are blocked by a router somewhere).

After running that command, a new file will be created (hops) containing the number of hops to each domain that completed successfully. The count.py script adds up all of the numbers in the hops file and divides that by the number of lines in the file (number of traceroutes that completed successfully) and prints out the average number of hops.

```
./traceroute.sh
cat trace| grep --no-group-separator -B 1 "traceroute to" | grep -v "traceroute to" | grep -vF "30  * * *" | awk '{ print $1}' > hops
./count.py
```
