#!/bin/sh

# если количество аргументов = 1
if [ $# = 1 ]; then     
    curl https://api.hh.ru/vacancies/\?text\=${1/ /+}\&search_field\=name\&per_page\=20 | jq > hh.json
else
	echo "Usage: ./hh.sh 'data scientist'"
fi

