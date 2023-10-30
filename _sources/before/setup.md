# Setup

The setup for the tutorials will be described below. 

# Setup: how to run the tutorial

This tutorial's goal is to provide a wide introduction to the Open EO and Pangeo ecosystem. 
While participants will see all the core libraries and possibilities offered by the OpenEO and Pangeo software ecosystem, it is also important that they get some insights about what a OpenEO and Pangeo platform is and how to use it. 

 
We recommend running this tutorial using the OpenEO, CDEC and Pangeo-EOSC infrastructure.  We recommend users to create logins and try to connect them before the tutorial.   
Creating account and how to run the turorial no these infrastructure are detailed in next pages.  

This page will describe the ways of running the tutorial:

- Locally on your personal computer
- Using Binder services


## Running on your own computer

Most parts of this tutorial were designed to run with limited computer resources, so it is possible to run on your laptop.
It is a bit more complicated as you will have to install the software environment yourself. Also you will not be able to test real cloud distributed processing with Dask gateway.

Steps to run this tutorial on your own computer are listed below and demonstrated _through Linux commands only_:

1. git clone the pangeo-openeo-BiDS-2023 repository.
```bash
git clone https://github.com/pangeo-data/pangeo-openeo-BiDS-2023.git
```
2. Install the required software environment with micromamba. If you do not have micromamba, install it by following these instructions (see [https://docs.conda.io/en/latest/miniconda.html](https://mamba.readthedocs.io/en/latest/micromamba-installation.html)). Then create the environment, this can take a few minutes.
```bash
micromamba  create -n pangeo-openeo-BiDS-2023 -f pangeo-openeo-BiDS-2023/.binder/environment.yml
```
3. Launch a Jupyterlab notebook server from this environment.
```bash
conda activate pangeo-openeo-BiDS-2023
jupyter lab
```
4. Open a web browser and connect to the Jupyterlab provided URL (you should see it in the jupyter lab command outputs), something like: http://localhost:8888/lab?token=42fac6733c6854578b981bca3abf5152.
5. Navigate to pangeo-openeo-BiDS-2023/tutorial/ using the file browser on the left side of the Jupyterlab screen.

## Running using a Binderhub deployment

[Binderhub](https://binderhub.readthedocs.io/en/latest/) is a cloud service that allows users to share reproducible interactive computing environments from code repositories. It is generally used to enable other users to easily run your own code through Jupyter notebooks. 
It is a really cool service offered for free by several organisations (MyBinder through Jupyter, GESIS, etc.).

It is probably the easiest way to execute notebooks in this repository, as you only have to do one click to arrive in a Jupyterlab with all the necessary libraries.
However, the hardware resources of the public BinderHub are quite small, so you will not be able to grasp the full potential of the Pangeo software stack, and parts of the notebooks will be unavailable.

All the notebooks on the part1 section, for example ["Handling multi-dimensional arrays with xarray"](../part1/xarray_introduction.ipynb) have a rocket icon 🚀 at the top, from which you can select the Binder button to just run this notebook on the [GESIS Binder service](https://notebooks.gesis.org/binder/).

Alternatively, you can also directly click on the below buttons:

GESIS:

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/pangeo-data/pangeo-openeo-BiDS-2023/HEAD)

MyBinder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pangeo-data/pangeo-openeo-BiDS-2023/HEAD)

You will then have to navigate to the pangeo-openeo-BiDS-2023/tutorial/ folder using the file browser on the left side of the Jupyterlab screen.
