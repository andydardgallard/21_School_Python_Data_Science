#!/bin/sh

if [ -z "$1" ] #check if arg is zero
    then ARG="../ex00/hh.json"
    else ARG="$1"
fi


cat $ARG | jq -r -f filter.jq > "hh.csv"
