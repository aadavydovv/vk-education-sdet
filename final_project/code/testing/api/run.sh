#!/bin/bash

source ./misc/environment.sh

command="pytest tests_api -s -l -v --alluredir /tmp/allure"

if [ -n "$PYTEST_THREADS" ]; then
  command="$command -n $PYTEST_THREADS"
fi

if [ -n "$PYTEST_KEYWORD_TESTS_API" ]; then
  command="$command -k $PYTEST_KEYWORD_TESTS_API"
fi

if [ -n "$PYTEST_MARK_TESTS_API" ]; then
  command="$command -m $PYTEST_MARK_TESTS_API"
fi

$command || true
