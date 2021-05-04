#!/bin/bash

readonly PATH_DIR_OUTPUT="/tmp/parsed_log"
readonly PATH_DIR_REPO="$(dirname "$0")/../"
readonly TYPES_REQUESTS=('CONNECT' 'DELETE' 'GET' 'HEAD' 'OPTIONS' 'PATCH' 'POST' 'PUT' 'TRACE')

PATH_FILE_LOG="$PATH_DIR_REPO${1-../misc/access.log}"
IFS='|'

mkdir -p "$PATH_DIR_OUTPUT"

path_file_log_filtered="$PATH_DIR_OUTPUT/bash_filtered_log"
grep -E "^.*\"(${TYPES_REQUESTS[*]})" "$PATH_FILE_LOG" > $path_file_log_filtered
PATH_FILE_LOG="$path_file_log_filtered"

{
printf 'Общее количество запросов\n'
wc -l < "$PATH_FILE_LOG"

printf '\nОбщее количество запросов по типу\n'
for type in "${TYPES_REQUESTS[@]}"; do
  printf "$type - %s\n" "$(grep -c "^.*\"$type" < "$PATH_FILE_LOG")"
done

printf '\nТоп 10 самых частых запросов\n'
  grep -oP "^.*?\".*? \K.*?(?= )" "$PATH_FILE_LOG" \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -10 \
  | awk '{print $2 " - " $1}'

printf '\nТоп 5 самых больших по размеру запросов, которые завершились клиентской ошибкой\n'
  grep "^.*\".*\" 4" "$PATH_FILE_LOG" \
  | awk '{print $10 " " $0}' \
  | sort -nr \
  | head -5 \
  | awk '{print $8 " - " $10 " - " $1 " - " $2}'

printf '\nТоп 5 пользователей по количеству запросов, которые завершились серверной ошибкой\n'
  grep -oP "^.*?(?= .*?\".*?\" 5)" "$PATH_FILE_LOG" \
  | sort \
  | uniq -c \
  | sort -nr \
  | head -5 \
  | awk '{print $2 " - " $1}'
} > "$PATH_DIR_OUTPUT/by_bash"

rm $path_file_log_filtered
