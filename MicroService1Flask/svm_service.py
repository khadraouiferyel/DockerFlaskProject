from flask import Flask, request, jsonify
import base64
import joblib
import librosa
import numpy as np
from flask_cors import CORS
import io

app = Flask(__name__)

# Enable CORS for the app
CORS(app)


try:
    model = joblib.load('model_svm.pkl')
except Exception as e:
    model = None
    print(f"Error loading the model: {e}")

# Define the genres as per your model's training
genres = ["rock", "jazz", "pop", "classical", "hiphop", "blues", "country", "disco", "metal", "reggae"]

def predict_genre_from_wav(wav_music_bytes):
    try:
        wav_file = io.BytesIO(wav_music_bytes)
        # Convert the bytes to a signal using librosa
        signal, rate = librosa.load(wav_file, sr=None)  # sr=None to preserve original sampling rate

        # Extract Mel spectrogram features from the signal
        hop_length = 512
        n_fft = 2048
        n_mels = 128

        S = librosa.feature.melspectrogram(y=signal, sr=rate, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
        S_DB = librosa.power_to_db(S, ref=np.max)

        # Flatten the Mel spectrogram to match the input shape the model expects
        S_DB_flattened = S_DB.flatten()[:1200]  # Truncate or pad if needed

        # Make the prediction
        if model is None:
            raise Exception("Model is not loaded properly.")
        
        y_pred = model.predict([S_DB_flattened])[0]
        predicted_genre = genres[y_pred]

        return predicted_genre,200
    
    except Exception as e:
        return f"Error in predicting genre: {str(e)}", 500


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Check if the base64-encoded wav file is provided
        if 'wav_music' not in data:
            return jsonify({"error": "Le paramètre 'wav_music' est manquant."}), 400

        # Log the base64-encoded data length to check if it's received
        wav_music_base64 = data['wav_music']
        print(f"Received Base64 string of length: {len(wav_music_base64)}")

        # Decode the base64-encoded WAV music
        try:
            wav_music_bytes = base64.b64decode(wav_music_base64)
            print(f"Decoded {len(wav_music_bytes)} bytes from Base64")
        except Exception as e:
            return jsonify({"error": f"Error decoding base64: {str(e)}"}), 400

        # Get the predicted genre
        predicted_genre, status_code = predict_genre_from_wav(wav_music_bytes)

        if status_code != 200:
            return jsonify({"error": predicted_genre}), status_code

        return jsonify({"predicted_genre": predicted_genre})

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
