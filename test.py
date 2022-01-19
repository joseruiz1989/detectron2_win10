print("hello world!!!")

"""
pip install wheel
pip install torch
pip install torchvision
pip install torchaudio

pip install cudatoolkit==11.0

pip install opencv-python



conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
pip install -e .

pip install tensorflow-gpu==2.3.0
pip install tensorflow==2.3


"""

import tensorflow as tf

# tf.test.gpu_device_name()

import torch

torch.cuda.get_device_name(0)


