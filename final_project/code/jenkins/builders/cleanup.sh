#!/bin/bash

declare -a containers=(
  'myapp'
  'vk_api'
  'mysql'
  'selenoid'
)

for c in "${containers[@]}"; do
  docker container rm -f "$c"
done

docker network rm testnet
