#!/bin/bash

# Build script for danb
# Usage: ./build.sh

set -e

echo "Building danb..."

# Check if libcurl is available
if ! pkg-config --exists libcurl; then
    echo "Error: libcurl-dev is required. Install it with:"
    echo "  Ubuntu/Debian: sudo apt-get install libcurl4-openssl-dev"
    echo "  CentOS/RHEL: sudo yum install libcurl-devel"
    echo "  macOS: brew install curl"
    exit 1
fi

# Compile
g++ -o danb main.cpp -lcurl -O2 -static-libgcc -static-libstdc++

# Strip debug symbols
strip danb

echo "Build completed successfully!"
echo "Binary: ./danb"
echo "Usage: ./danb <pdb|cif|fasta> <UniProtID|PDBID> [-o output_path]"
