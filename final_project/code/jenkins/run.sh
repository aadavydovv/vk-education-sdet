#!/bin/bash

JJB_DIR="$(dirname "$0")/jjb"
jenkins-jobs --conf "$JJB_DIR/auth.ini" update "$JJB_DIR/job.yml"

curl -X POST -L --user admin:11c76634b216e960e7286fdbb5a84f7e6c http://0.0.0.0:8080/job/myapp_testing/build
