# pytorch compatibility

## Cuda version

Cuda version limit the usage of the torch installation. Need to check

    Cuda version:       cat /usr/local/cuda/version.txt
    Architecture:       uname -m
    Linux distribution: lsb_release -a



Conda  or  pip: https://pytorch.org/get-started/previous-versions/

### CUDA Mem

In PyTorch, CUDA memory allocation refers to the process of reserving memory on the GPU (Graphics Processing Unit) for storing tensors and other GPU-related data during computation. The allocated memory is used to perform parallel computations on the GPU, which can significantly accelerate deep learning training and inference.


    You can use PyTorch's torch.cuda.memory_allocated() and torch.cuda.max_memory_allocated() functions to monitor the amount of memory currently allocated and the peak memory usage, respectively.

Techniques:

    Minimizing unnecessary storage,
    Reducing batch sizes,
    Using mixed-precision training,
    Employing memory optimization libraries like NVIDIA's CUDA Memory Management Tools (CUDAMM).

### Cuda OOM

    torch.cuda.OutOfMemoryError: CUDA out of memory.
    Tried to allocate 512.00 MiB (GPU 0; 10.76 GiB total capacity;
    4.55 GiB already allocated; 423.44 MiB free; 4.67 GiB reserved in total by PyTorch)
    If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
    See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF


在PyTorch中，CUDA内存的划分可以分为以下几个部分：

总容量（total capacity）：指的是GPU设备上总共可用的内存容量。它表示GPU的物理内存大小，以字节为单位。在报错信息中，总容量为10.76 GiB（千兆字节）。

已分配内存（allocated memory）：指已经被PyTorch分配并正在使用的GPU内存量。这包括已经创建的张量、模型参数和其他GPU相关的数据。在报错信息中，已分配内存为4.55 GiB。

可用内存（free memory）：指GPU设备上当前未被使用的、可供分配的内存量。在报错信息中，可用内存为423.44 MiB（兆字节）。

预留内存（reserved memory）：指由PyTorch保留的GPU内存量。这是为了满足PyTorch内部运算的需要而提前预留的内存。在报错信息中，预留内存为4.67 GiB。
