# Basic

# Use sftp to transfer file

    sftp account_name@IP_address 
    password, 
    put xxxx , where xxxx is the path

# Connect jupyter in remote server

    Launch Jupyter Notebook from remote server, selecting a port number for <PORT>:
    # Replace <PORT> with your selected port number
    ** jupyter notebook --no-browser --port=<PORT> **
    For example, if you want to use port number 8080, you would run the following:

    jupyter notebook --no-browser --port=8080
    Or run the following command to launch with default port:

    jupyter notebook --no-browser
    Please note the port setting. You will need it in the next step.

    You can access the notebook from your remote machine over SSH by setting up a SSH tunnel. Run the following command from your local machine:

    # Replace <PORT> with the port number you selected in the above step
    # Replace <REMOTE_USER> with the remote server username
    # Replace <REMOTE_HOST> with your remote server address
    ssh -L 8080:localhost:<PORT> <REMOTE_USER>@<REMOTE_HOST>


# Github Repo Deployment

# Run IPYNB
    ipython -c "%run Use.ipynb"

# Env

    conda create --name RepoName python=3.9
    conda activate RepoName
    pip install -r requirements.txt
    pip3 install ipykernel

    python -m ipykernel install --user --name mmcls

# Conda env manipulate

    The easiest way to save the packages from an environment to be installed in another computer is:

    $ conda list -e > req.txt
    then you can install the environment using

    $ conda create -n <environment-name> --file req.txt
    if you use pip, please use the following commands: reference https://pip.pypa.io/en/stable/reference/pip_freeze/

    $ env1/bin/pip freeze > requirements.txt
    $ env2/bin/pip install -r requirements.txt

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


#Cmake issue

    target_compile_features The compiler feature "cxx_std_17" is not known to
    CXX compiler

    "GNU"

    version 4.8.5.

    solution:
    scl enable devtoolset-7 bash
    cmake .. -DCMAKE_CXX_COMPILER=`which g++` -DCMAKE_C_COMPILER=`which gcc`

    You may need to run the cmake command twice.
