#!/bin/sh

if [ -z "$1" ]
    then ARG="../ex01/hh.csv"
    else ARG="$1"
fi

cat $ARG | head -n 1 > "hh_sorted.csv"
cat $ARG | tail -n 20 | sort -t "," -k 2 -k 1n >> "hh_sorted.csv"