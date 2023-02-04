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

    # CUDA 10.2
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=10.2 -c pytorch
    # CUDA 11.3
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
    # CUDA 11.6
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
    # CPU Only
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch


https://pytorch.org/get-started/previous-versions/ 
