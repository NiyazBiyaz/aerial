#!/bin/bash

set -e

apt update && apt install wget git -y

if ! command -v getoptions >/dev/null; then
    cd /bin
    wget https://github.com/ko1nksm/getoptions/releases/download/v3.3.2/getoptions
    chmod +x getoptions
    cd /workspaces/aerial
fi


chmod +x ./scripts/dotnet.sh ./scripts/python.sh

./scripts/dotnet.sh
./scripts/python.sh -M 3.13 -m 5

cd /workspaces/aerial

echo "Done!"
