#!/bin/bash

chmod +x ./scripts/dotnet.sh ./scripts/python.sh

./scripts/dotnet.sh
./scripts/python.sh -M 3.13 -m 5

cd /workspaces/aerial
