#!/bin/bash

if which dotnet >/dev/null; then
    echo "dotnet is already installed"
else
    echo "Start installing dotnet"

    apt-get update -y && \
        apt-get install -y dotnet-sdk-8.0 -y
fi