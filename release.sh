#!/bin/bash

# Version management script for danb
# Usage: ./release.sh <version>
# Example: ./release.sh 1.0.0

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <version>"
    echo "Example: $0 1.0.0"
    exit 1
fi

VERSION="$1"
TAG="v$VERSION"

# Validate version format (basic check)
if ! [[ $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Error: Version must be in format X.Y.Z (e.g., 1.0.0)"
    exit 1
fi

# Check if we're in a git repository
if [ ! -d .git ]; then
    echo "Error: Not in a git repository"
    exit 1
fi

# Check if tag already exists
if git tag -l | grep -q "^$TAG$"; then
    echo "Error: Tag $TAG already exists"
    exit 1
fi

# Check if working directory has changes
if [ -n "$(git status --porcelain)" ]; then
    echo "Working directory has uncommitted changes:"
    git status --short
    echo ""
    read -p "Do you want to commit these changes and proceed? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Release cancelled. Please commit or stash changes manually."
        exit 1
    fi
    
    echo "Committing changes..."
    git add .
    git commit -m "Prepare for release $TAG"
else
    echo "Working directory is clean."
fi

echo "Creating release $TAG..."

# Create and push tag
git tag -a "$TAG" -m "Release version $VERSION

Features:
- Download protein structures in PDB/CIF format
- Download FASTA sequences
- Support for UniProt IDs and PDB IDs
- Automatic source detection
- Custom output path with -o option"

echo "Tag $TAG created successfully!"
echo "To trigger the GitHub Actions build, push the tag:"
echo "  git push origin $TAG"
echo ""
echo "To push both commits and tags:"
echo "  git push origin main && git push origin $TAG"
