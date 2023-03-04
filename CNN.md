
Dear all,

Besides git clone mmclassification repo to finish the CNN tutorial, you can also use our complete code "CNN_Tutorial_Code.zip" and upload it to cs gpu farm. Below are the detailed steps.

1. Download the zipped file "CNN_Tutorial_Code.zip" from https://moodle.hku.hk/mod/url/view.php?id=2622398 to your local computer.

2. Login cs gpu farm and run "hostname -I" to find the IP address.

3. Open the terminal in your local computer, use the sftp tool to upload the code to the cs jpu farm by "sftp your_cs_gpu_farm_account_name@IP_address", type in your password, then run "put xxxx .", where xxxx is the path of the  "CNN_Tutorial_Code.zip" in your local computer (For example, Downloads/CNN_Tutorial_Code.zip in my computer).

4. In your cs gpu farm, install unzip tool by "conda install unzip", and then unzip our code by "unzip CNN_Tutorial_Code.zip", then enter the unzipped folder by "cd Leture02_Image_Classification_Code". In "demo/image_demo.py", you need to add the code "print(result)".

5. Enter the gpu mode by "gpu-interactive" and create a virtual environment and install all the libraries as below,

conda create -n mmcls python=3.7 -y

conda activate mmcls

conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch

pip install mmcv==1.5.0

pip install mmcv-full==1.5.0

cd Leture02_Image_Classification_Code

pip install -e .

6. Add you virtual environment to jupyter lab.

pip3 install ipykernel

python -m ipykernel install --user --name mmcls

7. Run jupyter lab in the cs gpu farm as introduced in https://moodle.hku.hk/mod/resource/view.php?id=2622393.
8. In your jupyter lab, add a new .ipynb file by click on "File", “New”, "Notebook" and select the kernal called mmcls (It is called mmcls2 in my case).



9. Training you model by copy the following code in your .ipynb file, and then click on the run command to start training your model.
!python tools/train.py \

  --config 'configs/resnet/resnet18_flowers_bs128.py' \

  --work-dir 'output/resnet18_flowers_bs128'

10. After finishing training your model, you can evaluate your model by copying the following code in your .ipynb file. 
!python demo/image_demo.py \

  --img 'demo/image_0005.jpg' \

  --config 'configs/resnet/resnet18_flowers_bs128.py' \

  --checkpoint 'output/resnet18_flowers_bs128/epoch_199.pth'



11. Save your .ipynb file and download it to your local computer by right click on the file in the left column，and then choose "download'.

You can then submit your .ipynb file to the moodle with the training log and the printed evaluation result.
Please follow all the steps carefully, otherwise you may not be able to finish the tutorial.

Best regards,

Yuying
