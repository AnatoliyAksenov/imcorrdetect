import numpy as np
from keras.preprocessing.image import load_img
from keras.models import load_model

loaded_model = load_model("cifar10_e3.h5")

def border(img, height=2):
    h, w, c = img.shape

    im_bg = img
    #im_bg = (im_bg + 1) * 255  # e.g., make it white
    im_bg[:2,:,:] = np.zeros((2, w, c))
    im_bg[:,:2,:] = np.zeros((h, 2, c))
    im_bg[30:32,:,:] = np.zeros((2, w, c))
    im_bg[:,30:32,:] = np.zeros((h, 2, c))
    return img

def predict(img_path):
    
    img = load_img(img_path)  # this is a PIL image
    
    w, h = img.width, img.height
    iii = []

    # For each part of image do prediction and store result to arr
    for x in range(0,w, 32):
        col = []
        for y in range(0, h, 32):
            tmp = np.array(img.crop(box=(x, y, x + 32, y + 32)))
            
            tt = tmp.reshape((1,) + tmp.shape)

            pred = loaded_model.predict(tt)  
            pr, cl = np.amax(pred), np.argmax(pred)
            
            if cl == 1 and pr > .9:
                tmp = border(tmp, 2)
                
            if len(col) == 0:
                col = tmp
            else:
                col = np.append(col, tmp, axis=0)

        if len(iii) == 0:
            iii = col
        else:
            iii = np.append(iii, col, axis=1)

        
        return iii
