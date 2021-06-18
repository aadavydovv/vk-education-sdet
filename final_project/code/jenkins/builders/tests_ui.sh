#!/bin/bash

ALLURE_DIR="$WORKSPACE/allure"
mkdir -p "$ALLURE_DIR"
docker run --network testnet -v "$ALLURE_DIR":/tmp/allure myapp_testing_ui
