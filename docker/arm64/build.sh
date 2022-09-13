#!/bin/bash
export DOCKER_BUILDKIT=1
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

(cd $SCRIPT_DIR/.. && \
docker build \
--build-arg BASE_IMAGE=hal-9000:core-arm64 \
--platform linux/arm64/v8 \
-t "ros-vide:latest" \
.)