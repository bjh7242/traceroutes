#!/bin/bash

while read line
do
    traceroute -n $line >> trace
done < top500
