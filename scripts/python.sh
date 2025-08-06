#!/bin/bash

install_libs() {
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
}


install_python() {
    mkdir /tmp/python && cd /tmp/python

    wget https://www.python.org/ftp/python/$1/Python-$1.tgz && \
        tar xzf Python-$1.tgz && \
        cd Python-$1 && \
        CFLAGS="-O3 -march=native" ./configure --enable-optimizations --with-ensurepip=install && \
        make -j$(nproc) && make altinstall && \
        cd / && rm -rf /tmp/python

    python$2 -m venv /venv &&
        /venv/bin/pip install --upgrade pip
    }

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
    install_libs
    install_python -M $VERSION -m $MAJOR
else 
    echo "python$MAJOR is already installed"
fi


if [[ "$FORCE" == true ]]; then
    /venv/bin/pip install -r requirements.txt
fi
