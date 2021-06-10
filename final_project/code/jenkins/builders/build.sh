#!/bin/bash

BUILDER_DIR="$(dirname "$0")"
PROJECT_DIR="$BUILDER_DIR/../.."
INIT_ENVIRONMENT_SCRIPT="$BUILDER_DIR/scripts/init_environment.sh"

docker build --tag vk_api --build-arg port=1337 --file "$PROJECT_DIR/vk_api/Dockerfile" "$PROJECT_DIR"

bash "$INIT_ENVIRONMENT_SCRIPT" "$PROJECT_DIR/testing/api/misc/environment.sh"
docker build --tag myapp_testing_api --file "$PROJECT_DIR/testing/api/Dockerfile" "$PROJECT_DIR"

bash "$INIT_ENVIRONMENT_SCRIPT" "$PROJECT_DIR/testing/ui/misc/environment.sh"
docker build --tag myapp_testing_ui --file "$PROJECT_DIR/testing/ui/Dockerfile" "$PROJECT_DIR"
