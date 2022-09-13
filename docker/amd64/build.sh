#!/bin/bash
export DOCKER_BUILDKIT=1
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

(cd $SCRIPT_DIR/.. && \
docker build \
--build-arg BASE_IMAGE=hal-9000:core-amd64 \
--platform linux/amd64 \
-t "ros-vide:latest" \
.)