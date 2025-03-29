import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    WHATSAPP_API_KEY = os.getenv('WHATSAPP_API_KEY')
    WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
    
    # Database
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    
    # Application
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    PORT = int(os.getenv('PORT', 5000))
    
    # Content Generation
    MAX_TOKENS = 2000
    TEMPERATURE = 0.7
    
    # Supported Subjects
    SUBJECTS = [
        'coding',
        'visual_arts',
        'performing_arts',
        'financial_literacy',
        'science'
    ]
    
    # Difficulty Levels
    DIFFICULTY_LEVELS = [
        'beginner',
        'intermediate',
        'advanced'
    ]
    
    # Content Types
    CONTENT_TYPES = [
        'text',
        'video',
        'image',
        'code'
    ]
    
    # WhatsApp Message Templates
    WELCOME_MESSAGE = """Welcome to TAPBuddy! I'm your AI-powered learning assistant.
Type 'help' to see available options or choose a subject to start learning!"""
    
    HELP_MESSAGE = """Available options:
1. Coding - Learn programming and coding
2. Visual Arts - Explore drawing, painting, and design
3. Performing Arts - Learn music, dance, and theater
4. Financial Literacy - Understand money management
5. Science - Discover scientific concepts and experiments

Type any of these subjects to get started!""" 