# Basic
 
#Github Repo Deployment

# Env

    conda create --name RepoName python=3.9
    conda activate RepoName
    pip install -r requirements.txt

# Directory Setting

`
Data
Model
Config
Tools
Scripts
Out
`


# pytorch compatibility

v1.12.1
###Conda

    # CUDA 10.2
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=10.2 -c pytorch
    # CUDA 11.3
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
    # CUDA 11.6
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
    # CPU Only
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch

###pip

    # ROCM 5.1.1 (Linux only)
    pip install torch==1.12.0+rocm5.1.1 torchvision==0.13.0+rocm5.1.1 torchaudio==0.12.0 --extra-index-url  https://download.pytorch.org/whl/rocm5.1.1
    # CUDA 11.6
    pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
    # CUDA 11.3
    pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113
    # CUDA 10.2
    pip install torch==1.12.0+cu102 torchvision==0.13.0+cu102 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu102
    # CPU only
    pip install torch==1.12.0+cpu torchvision==0.13.0+cpu torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cpu

https://pytorch.org/get-started/previous-versions/ 


# Gcc complier

    Please run command “scl enable devtoolset-9 bash”.  The absolute path of g++ 9 is “/opt/rh/devtoolset-9/root/bin/g++”
