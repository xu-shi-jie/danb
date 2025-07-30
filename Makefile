# Makefile for danb

CXX = g++
CXXFLAGS = -O2 -std=c++11 -Wall -Wextra
LDFLAGS = -lcurl -static-libgcc -static-libstdc++
TARGET = danb
SOURCE = main.cpp

.PHONY: all clean install test

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCE) $(LDFLAGS)
	strip $(TARGET)

clean:
	rm -f $(TARGET)

install: $(TARGET)
	install -m 755 $(TARGET) /usr/local/bin/

test: $(TARGET)
	@echo "Testing danb..."
	@echo "Usage: ./$(TARGET) <pdb|cif|fasta> <UniProtID|PDBID>"
	@echo "Example: ./$(TARGET) pdb 1abc"

debug: $(SOURCE)
	$(CXX) -g -O0 -std=c++11 -Wall -Wextra -o $(TARGET)-debug $(SOURCE) $(LDFLAGS)

.SILENT: clean
