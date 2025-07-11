from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
comprehend = boto3.client('comprehend', region_name='us-east-1')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment']
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
