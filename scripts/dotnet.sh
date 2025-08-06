#!/bin/bash

if which dotnet >/dev/null; then
    echo "dotnet is already installed"
else
    apt-get update && \
        apt-get install -y dotnet-sdk-8.0
fi