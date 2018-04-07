# Install Tensorflow1.7-GPU for Ubuntu1604

## list  
- `ubuntu1604` + `GTX 960`  
- `nvidia driver 384.xxx`  
- `CUDA-9.0`  
- `cudnn-7.0`  
- `tensorflow 1.7`  
- `anaconda3 5.1.0`  
- `opencv3`  

## install GTX 960 driver via apt-get
[**Proprietary GPU Drivers**](https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa)  

Make sure to **disable** `fastboot` and `secure boot`,
if not, login loop issue will occur  

`sudo add-apt-repository ppa:graphics-drivers/ppa`  
`sudo apt-get update`  
`sudo apt-get install nvidia-384-dev`  
`sudo apt-get install freeglut3-dev`  
 

## install CUDA-9.0 via runfile
[CUDA-9.0](https://developer.nvidia.com/cuda-90-download-archive)  


`sudo ./cuda_9.0.176_384.81_linux.run`  
**note that**: no need to install nvidia driver, select `n`

**env setup**:
~vim ~/.bashrc~  
  + export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}  
  + export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}  


## install CUDNN-7.0
[CUDNN-7.0](https://developer.nvidia.com/rdp/cudnn-download)  

`tar xvf cudnn-9.0-linux-x64-v7.tgz`  
`cp include/* /usr/local/cuda/include/ -a`  
`cp lib64/* /usr/local/cuda/lib64/ -a`


## install anaconda3
`./Anaconda3-5.1.0-Linux-x86_64.sh`  
`conda update conda`  
`conda create -n tf python=3.6` 
`conda install numpy pandas scikit-learn scipy matplotlib scikit-image setuptools wheel`


## install tendorflow 1.7
`pip install -U --pre tensorflow-gpu`

## install keras
`pip install -U --pre keras`

## install opencv3
`conda install -c conda-forge/label/broken opencv`  

