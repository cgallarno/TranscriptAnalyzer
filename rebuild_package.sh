#!/bin/bash

# Step 1: Clean up previous builds
echo "Cleaning up old builds..."
rm -rf build dist *.egg-info

# Step 2: Rebuild the package
echo "Building the package..."
python3 setup.py sdist bdist_wheel

# Step 3: Install the package locally
echo "Installing the package..."
pip install --upgrade --force-reinstall dist/*.whl

echo "Package rebuilt and installed successfully!"

