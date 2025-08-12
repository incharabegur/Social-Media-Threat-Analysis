from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample threat keywords
THREAT_KEYWORDS = ["threat", "kill", "attack", "harm", "danger","hack","bomb","hijack","shoot","kidnap","harrasment","bitcoin","die"]

@app.route('/analyze', methods=['POST'])
def analyze_message():
    data = request.json
    sender_message = data.get('message', '')
    
    # Check for threats
    detected_threats = [word for word in THREAT_KEYWORDS if word in sender_message.lower()]
    threat_count = len(detected_threats)
    
    # Determine threat level
    if threat_count == 0:
        level = "Low"
        image = "C:/Users/dhrut/OneDrive/Desktop/final/static/no.jpg"  # Placeholder image for a safe message
    elif threat_count <= 1:
        level = "Medium"
        image = "C:/Users/dhrut/OneDrive/Desktop/final/static/medium.jpg"  # Placeholder image for a medium-level threat
    else:
        level = "High"
        image = "C:/Users/dhrut/OneDrive/Desktop/final/static/high.jpg"  # Placeholder image for a high-level threat

    response = {
        'status': 'threat_detected' if threat_count > 0 else 'safe',
        'sender_message': sender_message,
        'detected_threats': detected_threats,
        'threat_level': level,
        'image': image,
        'receiver_notification': f"Threat Level: {level} ({', '.join(detected_threats)})" if detected_threats else "Message is safe."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
