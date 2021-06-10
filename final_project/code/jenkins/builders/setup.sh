#!/bin/bash

PROJECT_DIR="$(dirname "$0")/../.."

docker network create --subnet=13.37.0.0/16 --gateway=13.37.0.111 --attachable=true --driver=bridge testnet

docker run -d --name mysql --network testnet -e MYSQL_ROOT_PASSWORD=pass -p 3306:3306 percona:latest

until mysql -h13.37.0.111 -P3306 -uroot -ppass < "$PROJECT_DIR/misc/script.sql" 2>&1 >/dev/null | grep -q "1007"; do
  echo "failed to make an initial connection to the mysql server, retrying..."
  sleep 1
done

docker run --network testnet -v "$PROJECT_DIR/misc/app_config":/tmp/app_config myapp /app/myapp --config=/tmp/app_config --setup

docker pull selenoid/chrome:90.0
docker run -d --network testnet --name selenoid -p 4444:4444 -v /var/run/docker.sock:/var/run/docker.sock -v "$PROJECT_DIR/selenoid/":/etc/selenoid/:ro aerokube/selenoid:latest-release -container-network testnet

docker run -d --network testnet --name vk_api -p 1337:1337 vk_api
docker run -d --network testnet --name myapp -p 7331:7331 -v "$PROJECT_DIR/misc/app_config":/tmp/app_config myapp /app/myapp --config=/tmp/app_config
