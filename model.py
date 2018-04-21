
from keras.preprocessing.image import load_img
from keras.models import load_model

loaded_model = load_model("cifar10_e3.h5")


def predict(img_path):
    
    img = load_img(img_path)  # this is a PIL image
    
    w, h = img.width, img.height
    arr = []

    # For each part of image do prediction and store result to arr
    for x in range(0,w, 32):
        row = []
        for y in range(0, h, 32):
            tmp = np.array(img.crop(box=(x, y, x + 32, y + 32)))
            
            tt = tmp.reshape((1,) + tmp.shape)

            pred = loaded_model.predict(tt)    
            row.append((tmp, np.amax(pred), np.argmax(pred)))
        arr.append(row)

    
    return arr
