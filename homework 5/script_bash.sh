#!/bin/bash

readonly PATH_DIR_OUTPUT="/tmp/parsed_log"
readonly PATH_DIR_REPO="$(dirname "$0")/../"
readonly PATH_FILE_LOG="$PATH_DIR_REPO""${1-../misc/access.log}"
readonly PATH_FILE_OUTPUT="$PATH_DIR_OUTPUT/by_bash"
readonly TYPES_REQUESTS=('GET' 'POST' 'PUT' 'HEAD' 'DELETE' 'PATCH' 'OPTION')

mkdir -p "$PATH_DIR_OUTPUT"

printf 'Общее количество запросов\n' > $PATH_FILE_OUTPUT
# так и не понял, что происходит на 110201 строке, поэтому решил отфильтровать (а не просто заюзать wc -l)
IFS='|'
grep -c -E "] \"(${TYPES_REQUESTS[*]})" "$PATH_FILE_LOG" >> $PATH_FILE_OUTPUT

printf '\nОбщее количество запросов по типу\n' >> $PATH_FILE_OUTPUT
for type in "${TYPES_REQUESTS[@]}"; do
  printf "$type - %s\n" "$(grep -c "] \"$type" < "$PATH_FILE_LOG")" >> $PATH_FILE_OUTPUT
done
