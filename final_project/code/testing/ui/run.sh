#!/bin/bash

source ./misc/environment.sh

command="pytest tests_ui -s -l -v --alluredir /tmp/allure"

if [ -n "$PYTEST_THREADS" ]; then
  command="$command -n $PYTEST_THREADS"
fi

if [ -n "$PYTEST_KEYWORD_TESTS_UI" ]; then
  command="$command -k $PYTEST_KEYWORD_TESTS_UI"
fi

if [ -n "$PYTEST_MARK_TESTS_UI" ]; then
  command="$command -m $PYTEST_MARK_TESTS_UI"
fi

$command || true
