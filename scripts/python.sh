#!/bin/bash

MAJOR=""
MINOR=""
FORCE=false
PIP=true

parser_definition() {
    setup REST   help:usage                  -- "Usage: python.sh [options] [arguments]"
    flag  FORCE  -f --force                  -- "Install anyway"
    flag  PIP    -P --install-pip-reqs       -- "Install python libs from requirement.txt"
    param MAJOR  -M --major-version required -- "Major python version (f.e. 3.13)"
    param MINOR  -m --minor-version required -- "Minor python version (f.e. 5)"
    disp  :usage -h --help                   -- "Show this message"
}

eval "$(getoptions parser_definition) exit 1"


VERSION="$MAJOR.$MINOR"


if [[ "$(python --version)" != "Python $VERSION" || "$FORCE" == true ]]; then
    echo "Start installing python$MAJOR"

    apt update && \
        apt install -y \
        build-essential \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        wget \
        libbz2-dev \
        cmake \
        git && \
        apt clean && rm -rf /var/lib/apt/lists/*


    mkdir /tmp/python && cd /tmp/python

    wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tgz && \
        tar xzf Python-$VERSION.tgz && \
        cd Python-$VERSION && \
        CFLAGS="-O3 -march=native" ./configure --enable-optimizations --with-ensurepip=install && \
        make -j$(nproc) && make altinstall && \
        cd / && rm -rf /tmp/python

    python$MAJOR -m venv /venv &&
        /venv/bin/pip install --upgrade pip

else 
    echo "python$MAJOR is already installed"
fi


if [[ "$FORCE" == true ]]; then
    echo "Start installing python requirements"

    /venv/bin/pip install -r requirements.txt
fi
