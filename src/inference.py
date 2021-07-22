import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras.models import load_model
from PIL import Image
#import sys


FOODS = ['chilli_crab',
         'curry_puff',
         'dim_sum',
         'ice_kacang',
         'kaya_toast',
         'nasi_ayam',
         'popiah',
         'roti_prata',
         'sambal_stingray',
         'satay',
         'tau_huay',
         'wanton_noodle']


def run(img_path , model):
    print("This ran")

    #img_path = sys.argv[1]
    #img_path = "./satay.jpeg"
    img = load_img(img_path)
    
    resized_img = process_img(img)

    pred_class , prob= make_pred(resized_img , model)

    food_predicted = FOODS[pred_class]

    print("This is {} ".format(food_predicted))
    return food_predicted , prob


def load_img(img_path):
    img = Image.open(img_path)

    return img

def get_model_path():
    
    model_path = 0
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for f in filenames:
            if f.find("h5") >0:
                model_path = dirpath + "/" + f
    if model_path ==0:
        raise FileNotFoundError
    return model_path

def get_model():

    model_path = get_model_path()
    model = keras.models.load_model(model_path)

    return model

def process_img(img):

    img = img.resize((224,224))
    img = img.convert('RGB')
    img_array = np.array(img).astype("float16")
    img_array = img_array / 255

    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def make_pred(img_array , model):

    model_path = get_model_path()

    predict = model.predict(img_array)

    pred_class = int(np.argmax(predict))

    prob = round(predict[0].tolist()[pred_class]) # convert numpy rry into list and extract the probability

    return pred_class , prob

if __name__ == "__main__":
    
    #img_path = sys.argv[1]
    #img_path = "./satay.jpg"
    print("this run")
    run()