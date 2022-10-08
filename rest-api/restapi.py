from flask import Flask, request, jsonify, make_response
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import uuid
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

filename_response = str(uuid.uuid4()) + ".png"
TARGET_SIZE = (128, 128)

# metriks evaluasi model menggunakan pnsr dan ssim
def psnr(pred, gt):
  return tf.image.psnr(pred, gt, max_val=1.0)

def ssim(pred, gt):
  return tf.image.ssim(pred, gt, max_val=1.0)

# load model
model = tf.keras.models.load_model("model_autoencoder.h5", custom_objects={"psnr": psnr, "ssim": ssim})

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './image_request/'
app.config['DESTINATION_FOLDER'] = './image_response/'

# predit model
def predict_image(img_path):
    file_image = tf.io.read_file(img_path)
    image = tf.image.decode_jpeg(file_image, channels=3) # matrix 3D
    image = tf.image.convert_image_dtype(image, dtype=tf.float32) # normalisasi image
    #height, width = image.shape[0], image.shape[1]

    image = tf.image.resize(image, TARGET_SIZE) # resize image
    pred = model(np.expand_dims(image, axis=0))
    y = np.squeeze(pred, axis=0)

    #y = tf.image.resize(y, (height,width)) # resize image
    return y

@app.route('/predict', methods=['POST'])
def API():
    # request method using POST
    if request.method == "POST":
        if request.json is None:
            return jsonify({"error" : "no image"})
        
        try:
            filejson = request.get_json()
            imageName = filejson["image"]
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], imageName)
            output_image = predict_image(img_path)
            tf.keras.preprocessing.image.save_img(os.path.join(app.config['DESTINATION_FOLDER'],filename_response), output_image)
            return make_response(jsonify({"predict_image":filename_response}),201)
        except FileNotFoundError as e:
            return make_response(jsonify({"error":str(e)}), 400)
        except Exception as e:
            print(e)
            return make_response(jsonify({"error": str(e)}), 500)
    
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)