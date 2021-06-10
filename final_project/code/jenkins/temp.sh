#!/bin/bash

JJB_DIR="$(dirname "$0")/jjb"

count=10
for i in $(seq $count); do
	curl -X POST -L --user admin:11c76634b216e960e7286fdbb5a84f7e6c http://0.0.0.0:8080/job/myapp_testing/buildWithParameters
	echo "done $i build(s)"
	sleep 300
done

