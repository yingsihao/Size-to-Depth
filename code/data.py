import skimage.io as sio
import matplotlib.pyplot as plt
import numpy as np
import h5py
from skimage.transform import resize

mat = 'nyu_depth_v2_labeled.mat'
data = h5py.File(mat)

def get_rgbd(idx, resr, resc):
    rgb_ = data['images'][idx]
    depth_ = data['depths'][idx]

    rgb = np.empty([480, 640, 3])
    rgb[:,:,0] = rgb_[0,:,:].T
    rgb[:,:,1] = rgb_[1,:,:].T
    rgb[:,:,2] = rgb_[2,:,:].T

    rgb = rgb.astype('float32')
    sio.imshow(rgb / 255)
    sio.show()
    rgb = resize(rgb/255, [resr,resc])*255#[105,140])*255
    depth = np.empty([480, 640, 3])
    depth[:,:,0] = depth_[:,:].T
    depth[:,:,1] = depth_[:,:].T
    depth[:,:,2] = depth_[:,:].T
    print("fuck")
    sio.imshow(depth_.T)
    sio.show()
    return (rgb, depth)

