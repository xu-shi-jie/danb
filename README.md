# Danb: a small tool for download protein data

Danb comes from the word "danbaizhi" in Chinese, which means "protein". It is a small tool for downloading protein data from UniProt and PDB databases.

## Features

- Download protein structures in PDB/CIF format
- Download protein sequences in FASTA format  
- Support for UniProt IDs and PDB IDs
- Automatic source detection (UniProt vs PDB)
- AlphaFold structure support for UniProt IDs

## Installation

### Download pre-built binary

Download the latest release from the [Releases page](https://github.com/xu-shi-jie/danb/releases).

```bash
# Extract and use
tar -xzf danb-linux-x64.tar.gz
./danb <format> <id>
```

### Build from source

**Prerequisites:**
- g++ compiler
- libcurl development headers

**On Ubuntu/Debian:**
```bash
sudo apt-get install build-essential libcurl4-openssl-dev
```

**Build:**
```bash
# Using Makefile
make

# Or using build script
./build.sh

# Or manually
g++ -o danb main.cpp -lcurl -O2
```

## Usage

```bash
danb <pdb|cif|fasta> <UniProtID|PDBID>
```

**Examples:**
```bash
# Download PDB structure by PDB ID
./danb pdb 1abc

# Download CIF structure by PDB ID  
./danb cif 1abc

# Download FASTA sequence by PDB ID
./danb fasta 1abc

# Download AlphaFold structure by UniProt ID
./danb pdb P12345

# Download FASTA sequence by UniProt ID
./danb fasta P12345
```

## Development

### Building
```bash
make          # Build release version
make debug    # Build debug version
make clean    # Clean build files
```

### Creating a release
```bash
# Create and tag a new version
./release.sh 1.0.0

# Push to trigger GitHub Actions build
git push origin main
git push origin v1.0.0
```

## Contributing

If you would like to contribute to Danb, please fork the repository and submit a pull request.

## License

Danb is licensed under the MIT License. See the LICENSE file for more information.