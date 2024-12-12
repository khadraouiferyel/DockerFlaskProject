from flask import Flask, request, jsonify
import base64
import numpy as np
import librosa
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Define genre labels (ensure this matches the labels used during training)
genre_labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 
                'jazz', 'metal', 'pop', 'reggae', 'rock']

# Load the VGG model (replace with your model path)
model = load_model('vgg19_gtzan_genre_classifier.h5')

try:
    model = joblib.load('model_vgg.pkl')
except Exception as e:
    model = None
    print(f"Error loading the model: {e}")

# Define the genres as per your model's training
genres = ["rock", "jazz", "pop", "classical", "hiphop", "blues", "country", "disco", "metal", "reggae"]

def predict_genre_from_wav(wav_music_bytes):
    try:
        # Decode the base64-encoded audio data
        decoded_audio = base64.b64decode(audio_data)

        # Load the WAV audio from bytes
        y, sr = librosa.load(io=decoded_audio, sr=None)  # sr will be automatically detected

        # Extract Mel spectrogram
        mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
        mel_spect_db = librosa.power_to_db(mel_spect, ref=np.max)

        return mel_spect_db

    except Exception as e:
        print(f"Error processing audio data: {e}")
        return None

def predict_genre(audio_data):
    # Preprocess the audio data
    preprocessed_audio = preprocess_audio_file(audio_data)
    if preprocessed_audio is None:
        return None

    # Reshape the spectrogram for model input (assuming the model expects 2D input)
    preprocessed_audio = np.expand_dims(preprocessed_audio, axis=0)  # Add batch dimension

    # Normalize pixel values (if necessary, adjust based on your model's preprocessing)
    preprocessed_audio = preprocessed_audio.astype('float32') / 255.0

    # Predict using the model
    predictions = model.predict(preprocessed_audio)
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_genre = genre_labels[predicted_class]

    # Return the predicted genre and confidence score
    confidence = np.max(predictions)
    return predicted_genre, confidence

@app.route('/predictVgg', methods=['POST'])
def predict():
    data = request.json['audio_data']
    predicted_genre, confidence = predict_genre(data)

    if predicted_genre:
        return jsonify({'genre': predicted_genre, 'confidence': confidence:.2f})
    else:
        return jsonify({'error': 'Error processing audio data'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)


