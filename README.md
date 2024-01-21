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
