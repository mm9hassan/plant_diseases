import tensorflow as tf
import pickle
import numpy as np


classes_name = pickle.load(open('class_names','rb'))






model=tf.keras.models.load_model('planes.h5')
class Picture_uploader():
    
    
        

    def predicion(file):
        image=tf.keras.preprocessing.image.load_img(file,target_size=(224,224,3))
        ary=tf.keras.preprocessing.image.img_to_array(image)
        result=model.predict(np.expand_dims(ary,axis=0))
        print(result)
        ans=np.argmax(result)
        return classes_name[ans]

    
       






class Take_picture_uploader(Picture_uploader):
    pass