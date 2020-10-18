from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.models import load_model
from tensorflow import keras
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a data generator
# datagen = ImageDataGenerator(
    # rotation_range=10,
    # width_shift_range=0.1,
    # height_shift_range=0.1,
    # shear_range=0.0,
    # zoom_range=0.1,
    # horizontal_flip=True,
    # vertical_flip=True)
datagen = ImageDataGenerator ()
# Load and iterate training dataset
train_red = datagen.flow_from_directory('data_red/train/', target_size=(90, 90), color_mode='grayscale', class_mode='categorical', batch_size=128)
# Load and iterate validation dataset
val_red = datagen.flow_from_directory('data_red/validation/', target_size=(90, 90), color_mode='grayscale', class_mode='categorical', batch_size=128)
# Load and iterate test dataset
test_red = datagen.flow_from_directory('data_red/test/', target_size=(90, 90), color_mode='grayscale', class_mode='categorical', batch_size=128)
# confirm the iterator works
# batchX, batchy = train_red.next()
# print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))
class_list = list(test_red.class_indices.keys())


# Initialize the model
model_red = keras.Sequential ()
model_red.add(Conv2D(filters=16, kernel_size=3, padding='same', activation='relu', input_shape=(90,90,1)))
model_red.add(BatchNormalization())

model_red.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model_red.add(Conv2D(filters=16, kernel_size=3, padding='same', activation='relu'))
model_red.add(BatchNormalization())

model_red.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model_red.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'))
model_red.add(BatchNormalization())
model_red.add(Flatten())
model_red.add(Dense(7, activation='softmax'))


# Set training process params
batch_size = 128
epochs = 10

# Set the training configurations: optimizer, loss function, accuracy metrics
model_red.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

history = model_red.fit(train_red,
                     batch_size=batch_size, 
                     epochs=epochs, verbose=1, 
                     validation_data=val_red
          )
# save model and architecture to single file
model_red.save("model_red.h5")
print("Saved model to disk")
del model_red

# Check the model results on the test set
# load model
model_red = load_model('model_red.h5')
model_red.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# summarize model.
# model_red.summary()


model_red.evaluate(test_red)
X = cv2.imread('data_red/test/Elephant/r11.jpg', 0);
# cv2.imshow('detected circles',X)
# cv2.waitKey(0)
X = np.reshape(X,[1,90,90,1])
print(class_list[model_red.predict_classes(X)[0]])