from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from PIL import Image
import numpy as np
import io
import tensorflow as tf

graph = tf.get_default_graph()

class ImageClassifier:
    def __init__(self):
        with graph.as_default():
            self.model = MobileNet()
    def classify(self, img_storage):
        with graph.as_default():
            with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                sess.run(tf.local_variables_initializer())
                sess.run(tf.tables_initializer())
                keras.backend.set_session(sess)
                img = Image.open(io.BytesIO(img_storage.read()))
                img = img.resize((224, 224))
                x = image.img_to_array(img)
                print(x)
                x = np.expand_dims(x, axis=0)
                preds = self.model.predict(x)
        return decode_predictions(preds, top=3)[0]

