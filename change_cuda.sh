#!/bin/bash

# Check if CUDA version argument is provided
if [ $# -eq 0 ]; then
  echo "CUDA version argument is required."
  exit 1
fi

# Read CUDA version from command-line argument
cuda_version=$1

# Set the CUDA environment variables
export PATH=/usr/local/cuda-$cuda_version/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-$cuda_version/lib64

# Source the .bashrc file to ensure the changes take effect
source .bashrc

# Perform your tasks here
# ...

# Print a completion message
echo "CUDA tasks completed."
