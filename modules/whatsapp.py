import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class WhatsAppHandler:
    def __init__(self):
        self.api_key = os.getenv('WHATSAPP_API_KEY')
        self.api_url = "https://graph.facebook.com/v17.0"
        self.phone_number_id = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
        
    def process_message(self, data):
        """Process incoming WhatsApp messages"""
        try:
            # Extract message details
            message = data['entry'][0]['changes'][0]['value']['messages'][0]
            sender_id = message['from']
            message_text = message['text']['body'].lower()
            
            # Process the message and generate response
            response = self._generate_response(message_text)
            
            # Send response back to user
            self.send_message(sender_id, response)
            
            return {
                'success': True,
                'message': 'Message processed successfully'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _generate_response(self, message_text):
        """Generate appropriate response based on user message"""
        # Basic command processing
        if 'help' in message_text:
            return self._get_help_message()
        elif 'coding' in message_text:
            return self._get_subject_menu('coding')
        elif 'art' in message_text:
            return self._get_subject_menu('visual_arts')
        elif 'performing' in message_text:
            return self._get_subject_menu('performing_arts')
        elif 'finance' in message_text:
            return self._get_subject_menu('financial_literacy')
        elif 'science' in message_text:
            return self._get_subject_menu('science')
        else:
            return "Welcome to TAPBuddy! Please type 'help' to see available options."
    
    def _get_help_message(self):
        """Generate help message with available options"""
        return """Welcome to TAPBuddy! Here are the available options:
        
1. Coding - Learn programming and coding
2. Visual Arts - Explore drawing, painting, and design
3. Performing Arts - Learn music, dance, and theater
4. Financial Literacy - Understand money management
5. Science - Discover scientific concepts and experiments

Type any of these subjects to get started!"""
    
    def _get_subject_menu(self, subject):
        """Generate subject-specific menu"""
        menus = {
            'coding': """Coding Topics:
1. Python Basics
2. Web Development
3. Mobile Apps
4. Data Structures
5. Algorithms

Type a number to learn about that topic!""",
            'visual_arts': """Visual Arts Topics:
1. Drawing Basics
2. Color Theory
3. Digital Art
4. Photography
5. Design Principles

Type a number to learn about that topic!""",
            'performing_arts': """Performing Arts Topics:
1. Music Theory
2. Dance Basics
3. Theater Acting
4. Public Speaking
5. Performance Skills

Type a number to learn about that topic!""",
            'financial_literacy': """Financial Literacy Topics:
1. Budgeting
2. Saving Money
3. Investment Basics
4. Banking
5. Personal Finance

Type a number to learn about that topic!""",
            'science': """Science Topics:
1. Physics Basics
2. Chemistry
3. Biology
4. Environmental Science
5. Scientific Method

Type a number to learn about that topic!"""
        }
        return menus.get(subject, "Invalid subject. Please try again.")
    
    def send_message(self, recipient_id, message):
        """Send message to WhatsApp user"""
        url = f"{self.api_url}/{self.phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": recipient_id,
            "type": "text",
            "text": {"body": message}
        }
        
        response = requests.post(url, headers=headers, json=data)
        return response.json() 