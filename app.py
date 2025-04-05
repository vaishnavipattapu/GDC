from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from modules.content_generator import ContentGenerator
from modules.whatsapp import WhatsAppHandler
from modules.database import Database

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize components
content_generator = ContentGenerator()
whatsapp_handler = WhatsAppHandler()
database = Database()

@app.route('/api/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.json
        subject = data.get('subject')
        topic = data.get('topic')
        difficulty = data.get('difficulty', 'beginner')
        
        # Generate content based on subject
        content = content_generator.generate(subject, topic, difficulty)
        
        # Store in database
        content_id = database.store_content(content)
        
        return jsonify({
            'success': True,
            'content_id': content_id,
            'content': content
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/whatsapp/webhook', methods=['POST'])
def whatsapp_webhook():
    try:
        data = request.json
        # Process incoming WhatsApp message
        response = whatsapp_handler.process_message(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/content/<content_id>', methods=['GET'])
def get_content(content_id):
    try:
        content = database.get_content(content_id)
        if content:
            return jsonify({
                'success': True,
                'content': content
            })
        return jsonify({
            'success': False,
            'error': 'Content not found'
        }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 5000))) 