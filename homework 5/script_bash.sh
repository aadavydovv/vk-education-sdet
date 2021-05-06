#!/bin/bash

readonly PATH_DIR_OUTPUT="/tmp/parsed_log"
readonly PATH_FILE_LOG="$(dirname "$0")/../${1-../misc/access.log}"
readonly IFS='|'

mkdir -p "$PATH_DIR_OUTPUT"

{
printf 'Общее количество запросов\n'
wc -l < "$PATH_FILE_LOG"

printf '\nОбщее количество запросов по типу\n'
grep -oP "^.*?\"\K.*?(?= )" "$PATH_FILE_LOG" | sort | uniq -c | awk '{print $2 " - " $1}'

printf '\nТоп 10 самых частых запросов\n'
grep -oP "^.*?\".*? \K.*?(?= )" "$PATH_FILE_LOG" | sort | uniq -c | sort -nr | head -10 | awk '{print $2 " - " $1}'

printf '\nТоп 5 самых больших по размеру запросов, которые завершились клиентской ошибкой\n'
grep "^.*\".*\" 4" "$PATH_FILE_LOG" | awk '{print $10 " " $0}' | sort -nr | head -5 | awk '{print $8 " - " $10 " - " $1 " - " $2}'

printf '\nТоп 5 пользователей по количеству запросов, которые завершились серверной ошибкой\n'
grep -oP "^.*?(?= .*?\".*?\" 5)" "$PATH_FILE_LOG" | sort | uniq -c | sort -nr | head -5 | awk '{print $2 " - " $1}'
} > "$PATH_DIR_OUTPUT/by_bash"
