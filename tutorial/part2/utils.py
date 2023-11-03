import os
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


def load_data(path):
    files = [path + file for file in os.listdir(path) if "EU" in file]
    dataset = [xr.open_dataset(file, chunks={}).expand_dims("t") for file in files]
    data = xr.combine_by_coords(dataset)
    return data


def tone_mapping(B04,B03,B02):
    red = B04.values
    green = B03.values
    blue = B02.values
    red = (red+1)/1733*255
    green = (green+1)/1630*255
    blue = (blue+1)/1347*255
    red = np.clip(red,0,255).astype(np.uint8)
    green = np.clip(green,0,255).astype(np.uint8)
    blue = np.clip(blue,0,255).astype(np.uint8)
    brg = np.zeros((red.shape[0],red.shape[1],3),dtype=np.uint8)
    brg[:,:,0] = red
    brg[:,:,1] = green
    brg[:,:,2] = blue
    return brg