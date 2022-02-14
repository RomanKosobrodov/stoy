# stoy
Sagemaker Studio Auto Shutdown extension.

## Installation

Python development package is required to build the extension. The example below is for CentOS. 
On other operating systems the package name can differ.

Set the timeout in minutes `SAGEMAKER_TIMEOUT_MINUTES` if you want to change the default value of 60 min.

```bash
yum install -y python36-devel.x86_64
SAGEMAKER_TIMEOUT_MINUTES=2
pip install git+https://github.com/RomanKosobrodov/stoy.git
jupyter serverextension enable --py sagemaker_studio_autoshutdown
```
