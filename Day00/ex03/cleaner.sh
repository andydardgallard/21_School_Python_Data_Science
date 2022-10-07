#!/bin/sh

if [ -z "$1"]
    then ARG="../ex02/hh_sorted.csv"
    else ARG="$1"
fi

cleaner()
{
    awk -F "\"," 'BEGIN{
        OFS = FS}{
        if (tolower($3) ~ "junior" && tolower($3) ~ "middle" && tolower($3) ~ "senior")
            $3 = "\"Junior/Middle/Senior"
        else if (tolower($3) ~ "junior" && tolower($3) ~ "middle")
            $3 = "\"Junior/Middle"
        else if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
            $3 = "\"Junior/Senior"
        else if (tolower($3) ~ "middle" && tolower($3) ~ "senior")
            $3 = "\"Middle/Senior"
        else if (tolower($3) ~ "junior")
            $3 = "\"Junior"
        else if (tolower($3) ~ "senior")
            $3 = "\"Senior"
        else if (tolower($3) ~ "middle")
            $3 = "\"Middle"
        else
            $3 = "\"-"
        print $0}'
}

cat $ARG | head -n 1 > "hh_positions.csv"
cat < $ARG | while read -r; do cleaner >> "hh_positions.csv"; done
