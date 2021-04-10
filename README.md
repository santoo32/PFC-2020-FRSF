<h2 align="center"><code>🧑‍🎓UTN - FRSF🎉!</code></h2>
<p align="center"><i>while(noSuccess){ tryAgain() }</i> 
  ----- A t-shirt</p>
<p align="center">
  <a href=https://github.com/santoo32/PFC-2020-FRSF/tree/master">
    <img src="https://img.shields.io/badge/Branch-master-green.svg?longCache=true"
        alt="Branch">
  </a>
  <a href="https://github.com/santoo32/PFC-2020-FRSF/stargazers">
    <img src="https://img.shields.io/github/stars/YunYang1994/TensorFlow2.0-Examples.svg?label=Stars&style=social"
        alt="Stars">
  </a>
    <a href="https://github.com/santoo32/PFC-2020-FRSF/network/members">
    <img src="https://img.shields.io/github/forks/YunYang1994/TensorFlow2.0-Examples.svg?label=Forks&style=social"
        alt="Forks">
  </a>
  </a>
   <a href="https://github.com/sindresorhus/awesome">
   <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"
        alt="Awesome">
  </a>
  </a>
   <a href="https://github.com/santoo32/PFC-2020-FRSF/blob/master/LICENSE">
</p>
<div align="center">
  <sub>Created by
   <div>
    <a href="https://github.com/santoo32">santoo32</a>
   </div>
   <div>
    <a href="https://github.com/farca9">farca9</a>
   </div>
</div>
<br>
    
This repository was created for what will be the development of our final degree project

## Contents

#### Object Detection
For the core of our aplication we used:
- **YOLOv3** ([paper](https://arxiv.org/pdf/1804.02767.pdf)). YOLOv3: An Incremental Improvement.

<p align="center">
    <img width="65%" src="https://user-images.githubusercontent.com/30433053/67914531-656bb080-fbcb-11e9-9775-302a25faf747.png" style="max-width:65%;">
    </a>
</p>

## Requirements:

#### Hardware:
- CUDA compatible NVIDIA GPU (https://developer.nvidia.com/cuda-gpus)

#### Software Dependencies:
- <a href="https://www.python.org/downloads/">Python 3.5.x - 3.8.x</a>
- <a href="https://developer.nvidia.com/cuda-10.1-download-archive-base">CUDA Toolkit 10.1</a>
- <a href="https://developer.nvidia.com/rdp/cudnn-archive">cuDNN 7.6.5</a>
- (Optional) <a href="https://www.anaconda.com/">Anaconda Environment 4.8.x</a> -- to handle Python environment and dependencies

This project is done with Tensorflow 2.2.0. There are other possible depency configurations that **might** work, check:
- Linux/macOS: https://www.tensorflow.org/install/source#gpu
- Windows: https://www.tensorflow.org/install/source_windows#gpu

## How to run:

These steps may vary depending on OS and use/not use of Anaconda Environment.
If you are using Anaconda to handle dependencies, steps 2 and 6 need to be run inside the Conda Virtual Environment.

1. Clone the git repo
2. Install requirements: `pip3 install -r ./docs/requirements.txt`
3. Download model: https://drive.google.com/drive/folders/1VU51VJXfGMfdwdOFZov6TSXh-rRUmWbC
4. Extract model.weights in /data/weights
5. Rename model.weights to handgun.weights
6. Run: `python MainWIndowAlpha.py`
