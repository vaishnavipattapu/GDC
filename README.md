# TAP AI Content Generator

An AI-powered solution for generating educational content for The Apprentice Project (TAP), delivering personalized learning materials through WhatsApp.

## Features

- AI-powered content generation for:
  - Visual Arts
  - Performing Arts
  - Coding
  - Financial Literacy
  - Science
- WhatsApp integration for content delivery
- Personalized learning paths
- Video tutorial generation
- Code snippet generation
- Design idea generation

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   WHATSAPP_API_KEY=your_whatsapp_api_key
   MONGODB_URI=your_mongodb_uri
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Project Structure

```
├── app.py                 # Main application file
├── config.py             # Configuration settings
├── requirements.txt      # Project dependencies
├── modules/
│   ├── content_generator/  # AI content generation modules
│   ├── whatsapp/          # WhatsApp integration
│   └── database/          # Database operations
└── templates/            # HTML templates
```

## API Endpoints

- `/api/generate-content`: Generate educational content
- `/api/whatsapp/webhook`: WhatsApp webhook endpoint
- `/api/content/:id`: Get specific content

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 