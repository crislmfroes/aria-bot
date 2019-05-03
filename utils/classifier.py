from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from io import BytesIO

class ImageClassifier:
    def __init__(self):
        self.model = MobileNet()
    def classify(self, img_storage):
        byte_storage = BytesIO(img_storage.read())
        byte_storage.seek(0)
        img = Image.open(byte_storage)
        img = img.resize((224, 224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        predictions = self.model.predict(x)
        return decode_predictions(predictions)