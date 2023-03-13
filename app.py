from flask import Flask, render_template, request
from tensorflow import keras
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = keras.models.load_model('my_model.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the image file from the POST request
        image_file = request.files['image']

        # Open the image file and convert it to grayscale
        image = Image.open(image_file).convert('L')

        # Resize the image to 28x28 and convert it to a NumPy array
        image = image.resize((28, 28))
        image = np.array(image)

        # Preprocess the image
        image = image.reshape(1, 28, 28, 1) / 255.0

        # Use the trained model to make a prediction
        prediction = np.argmax(model.predict(image))

        # Render the result template with the predicted class label
        return render_template('result.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
