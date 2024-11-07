from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Simuler le chargement d'un modèle SVM (ici, ce sera statique pour le moment)
# Normalement, on chargerait le modèle avec joblib ou pickle

@app.route('/predict', methods=['POST'])
def predict_genre():
    data = request.get_json()

    if 'wav_music' not in data:
        return jsonify({"error": "Le paramètre 'wav_music' est manquant."}), 400

    wav_music_base64 = data['wav_music']
    wav_music_bytes = base64.b64decode(wav_music_base64)

    predicted_genre = "Jazz"  
    return jsonify({"predicted_genre": predicted_genre})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
