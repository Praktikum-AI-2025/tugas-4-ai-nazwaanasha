# =====================================================================================================
# Membangun sebuah model Neural Network untuk klasifikasi dataset Horse or Human dalam binary classes.
#
# Input layer harus menerima 150x150 dengan 3 bytes warna sebagai input shapenya.
# Jangan menggunakan lambda layers dalam model.
#
# Dataset yang digunakan dibuat oleh Laurence Moroney (laurencemoroney.com).
#
# Standar yang harus dicapai untuk accuracy dan validation_accuracy > 83%
# =====================================================================================================

import urllib.request
import zipfile
import tensorflow as tf
import os
from keras_preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop


def solution_05():
    data_url_1 = 'https://github.com/dicodingacademy/assets/releases/download/release-horse-or-human/horse-or-human.zip'
    urllib.request.urlretrieve(data_url_1, 'horse-or-human.zip')
    local_file = 'horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/horse-or-human')

    data_url_2 = 'https://github.com/dicodingacademy/assets/raw/main/Simulation/machine_learning/validation-horse-or-human.zip'
    urllib.request.urlretrieve(data_url_2, 'validation-horse-or-human.zip')
    local_file = 'validation-horse-or-human.zip'
    zip_ref = zipfile.ZipFile(local_file, 'r')
    zip_ref.extractall('data/validation-horse-or-human')
    zip_ref.close()

    TRAINING_DIR = 'data/horse-or-human'
    train_datagen = ImageDataGenerator(
        rescale=1/255,
        rotation_range=40,
        horizontal_flip=True,
        shear_range=0.2,
        zoom_range=0.2,
        fill_mode='nearest'
    )

    train_generator= ImageDataGenerator(rescale=1./255)
    
    # YOUR CODE HERE

    model=tf.keras.models.Sequential([
        # YOUR CODE HERE, end with a Neuron Dense, activated by sigmoid

                tf.keras.layers.Dense(1, activation='sigmoid') #DO NOT CHANGE THIS LINE!
        ])

    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model=solution_05()
    model.save("model_05.h5")
