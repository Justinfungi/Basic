import torch
import torchvision
import subprocess

def check_versions():
    # Check PyTorch version
    print(f"PyTorch version: {torch.__version__}")

    # Check torchvision version
    print(f"torchvision version: {torchvision.__version__}")

    # Check CUDA version
    print(f"CUDA version: {torch.version.cuda}")

    # Check NVCC version
    try:
        nvcc_version = subprocess.check_output(["nvcc", "--version"]).decode().strip()
        print(f"NVCC version: {nvcc_version}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("NVCC version: Not available")

if __name__ == "__main__":
    check_versions()