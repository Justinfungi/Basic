# Basic

## Remote server and Local server

kill -9 $(lsof -t -i:8080)


### Use sftp to transfer file

    sftp account_name@IP_address 
    password, 
    put xxxx , where xxxx is the path

### Connect jupyter in remote server

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



## Github Repo Deployment

### Run IPYNB
    ipython -c "%run Use.ipynb"
    
# Directory Setting
`
Data
Model
Config
Tools
Scripts
Out
`

## Conda Usage
### Env install

    conda create --name jusjus python=3.9
    conda activate jusjus
    pip install -r requirements.txt
    pip3 install ipykernel

    python -m ipykernel install --user --name jusjus

### Conda env manipulate

    The easiest way to save the packages from an environment to be installed in another computer is:

    $ conda list -e > req.txt
    then you can install the environment using

    $ conda create -n <environment-name> --file req.txt
    if you use pip, please use the following commands: reference https://pip.pypa.io/en/stable/reference/pip_freeze/

    $ env1/bin/pip freeze > requirements.txt
    $ env2/bin/pip install -r requirements.txt
    
### Env delete
    conda remove --name ENV_NAME --all
    
### Install requirement.txt by conda
    
    ``` bash
    conda uses an environment.yaml file instead of requirements.txt, but you can include one in the other:

    # environment.yaml

    name: test-env
    channels:
      - conda-forge
    dependencies:
      - python>=3.5
      - anaconda
      - pip
      - pip:
        - -r file:requirements.txt
    Then use conda to create the environment via

    conda env create -f environment.yaml
    ```


# pytorch compatibility

v1.12.1
### Conda

    # CUDA 10.2
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=10.2 -c pytorch
    # CUDA 11.3
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
    # CUDA 11.6
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
    # CPU Only
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch
    
    # Remove all env
    for i in `conda env list|awk '{print $1}'|egrep -v 'base|#'|tr '\n' ' '`;do echo $i;conda env remove --name $i;done

### pip

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


## Gcc complier

    Please run command “scl enable devtoolset-9 bash”.  The absolute path of g++ 9 is “/opt/rh/devtoolset-9/root/bin/g++”


### Cmake issue

    target_compile_features The compiler feature "cxx_std_17" is not known to
    CXX compiler
    
    

    "GNU"

    version 4.8.5.

    solution:


    
    scl enable devtoolset-7 bash
    cmake .. -DCMAKE_CXX_COMPILER=`which g++` -DCMAKE_C_COMPILER=`which gcc`

    You may need to run the cmake command twice.


### CUDA

In PyTorch, CUDA memory allocation refers to the process of reserving memory on the GPU (Graphics Processing Unit) for storing tensors and other GPU-related data during computation. The allocated memory is used to perform parallel computations on the GPU, which can significantly accelerate deep learning training and inference.

PyTorch **utilizes the CUDA runtime API provided by NVIDIA** to manage GPU memory. When you create a tensor or perform operations that require GPU memory, PyTorch interacts with the CUDA runtime to allocate the necessary memory space on the GPU.

The CUDA memory allocation in PyTorch can be categorized into two types: managed memory and pinned memory.

**Managed Memory**: Managed memory refers to the default memory allocation strategy in PyTorch. When you create a tensor on the GPU, PyTorch automatically handles the memory allocation and deallocation. It dynamically allocates GPU memory as needed and releases the memory when it is no longer required. This managed memory allocation is convenient but may have some overhead due to the dynamic allocation process.

**Pinned Memory**: Pinned memory, also known as page-locked memory, is a specialized memory allocation technique that can be used in PyTorch to improve data transfer between the CPU and GPU. Pinned memory resides in the system's physical memory (RAM) and is accessible by both the CPU and GPU. It helps to reduce the overhead associated with data transfers between the host (CPU) and device (GPU). Pinned memory can be explicitly allocated using the torch.cuda.pinned_memory function.

The amount of CUDA memory reserved by PyTorch depends on various factors, including the size and type of tensors, model architecture, and the specific operations being performed. PyTorch estimates the memory requirements for tensors and tries to allocate the necessary memory space accordingly. However, it's important to monitor GPU memory usage to avoid exceeding the available memory capacity, which could lead to out-of-memory errors.

    You can use PyTorch's torch.cuda.memory_allocated() and torch.cuda.max_memory_allocated() functions to monitor the amount of memory currently allocated and the peak memory usage, respectively.

If you encounter memory allocation issues or want to optimize memory usage in PyTorch, you can consider techniques such as minimizing unnecessary storage, reducing batch sizes, using mixed-precision training, or employing memory optimization libraries like NVIDIA's CUDA Memory Management Tools (CUDAMM).

Overall, PyTorch provides a convenient interface for CUDA memory allocation, allowing you to leverage the power of GPUs for efficient deep learning computations.

#### Cuda OOM

    torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 512.00 MiB (GPU 0; 10.76 GiB total capacity; 4.55 GiB already allocated; 423.44 MiB free; 4.67 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF


在PyTorch中，CUDA内存的划分可以分为以下几个部分：

总容量（total capacity）：指的是GPU设备上总共可用的内存容量。它表示GPU的物理内存大小，以字节为单位。在报错信息中，总容量为10.76 GiB（千兆字节）。

已分配内存（allocated memory）：指已经被PyTorch分配并正在使用的GPU内存量。这包括已经创建的张量、模型参数和其他GPU相关的数据。在报错信息中，已分配内存为4.55 GiB。

可用内存（free memory）：指GPU设备上当前未被使用的、可供分配的内存量。在报错信息中，可用内存为423.44 MiB（兆字节）。

预留内存（reserved memory）：指由PyTorch保留的GPU内存量。这是为了满足PyTorch内部运算的需要而提前预留的内存。在报错信息中，预留内存为4.67 GiB。
