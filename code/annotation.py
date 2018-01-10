import skimage.io as io
import numpy as np

def get_label(rgb):
    (H, W, _) = rgb.shape
    label = []
    for div in (4, 10, 20):
        rgb_img = rgb.astype('float32')
        for row in range(int(round(H / div)), H, int(round(H / div))):
            rgb_img[row, :, :] = 255
        for col in range(int(round(W / div)), W, int(round(W / div))):
            rgb_img[:, col, :] = 255
        io.imshow(rgb_img / 255)
        io.show()

        size = np.zeros([div, div])
        for r in range(div):
            for c in range(div):
                size[r][c] = input()
        label.append(size)
    return label

def get_dense_label(rgb):
    print("get_dense_label")
    (H, W, _) = rgb.shape
    label = []
    sizes = [7]
    for div in sizes:
        rgb_img = rgb.astype('float32')
        for row in range(int(round(H / div)), H, int(round(H / div))):
            rgb_img[row, :, :] = 255
        for col in range(int(round(W / div)), W, int(round(W / div))):
            rgb_img[:, col, :] = 255
        io.imshow(rgb_img / 255)
        io.show()
        print("input %d" %div)
        size = np.zeros([div, div])
        '''
        for r in range(div):
            for c in range(div):
                size[r][c] = input("%d %d"%(r,c))
        print "input %d done" %div
        label.append(size)
        '''
    label = [[[1,2,2,1],[1,2,2,1],[1,2,2,1],[1,1.7,2,0.3]]]
    #label = [[[1,2,2,1],[1,1,1,1],[1,1,1,1],[1,1.7,2,0.3]]]
    label = [[[1, 1.2, 1.5, 1.5, 1.5, 1.5, 1.5],[0.9, 1.05, 1.5, 2, 2, 2, 2],[0.9, 1.1, 1.5, 2, 4, 4, 4],
              [0.9, 1.1, 1.3, 1.7, 2, 4, 3],[0.9, 1.1, 1.3, 1.8, 1.4, 1.4, 1.7],
              [1, 1.1, 1.3, 1.5, 1.5, 0.7, 0.7],[0.8, 1, 1.3, 1.5, 1, 0.6, 0.6]]]
    label = label[0]
    dense_arr = []
    for div in sizes:
        stepr = int(round(H/div))
        stepc = int(round(W/div))
        dense = np.zeros([H, W])
        for r in range(H):
            for c in range(W):
                pr = int(r/stepr)
                pc = int(c/stepc)
                dense[r][c] = label[pr][pc]
        dense_arr.append(dense)
    print("get_dense_label_done")
    return dense_arr[0]