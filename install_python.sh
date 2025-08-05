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

BASE_VERSION="3.13"
VERSION="$BASE_VERSION.5"
wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tgz && \
    tar xzf Python-$VERSION.tgz && \
    cd Python-$VERSION && \
    CFLAGS="-O3 -march=native" ./configure --enable-optimizations --with-ensurepip=install && \
    make -j$(nproc) && make altinstall && \
    cd / && rm -rf /tmp/python

python$BASE_VERSION -m venv /venv &&
    /venv/bin/pip install --upgrade pip
