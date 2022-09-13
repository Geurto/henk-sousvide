#!/bin/bash
set -e

# setup ros2 environment
source "/entrypoint.sh" --
source "/henk/install/setup.bash" --
exec "$@"