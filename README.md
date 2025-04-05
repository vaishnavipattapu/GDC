# TAPBuddy - AI-Powered Learning Assistant

TAPBuddy is an intelligent learning assistant that provides personalized educational content across multiple subjects using AI technology.

## Features

- 🎯 Multiple Subject Support
  - Coding
  - Visual Arts
  - Performing Arts
  - Financial Literacy
  - Science

- 🤖 AI-Powered Content Generation
  - Personalized learning content
  - Adaptive difficulty levels
  - Interactive chat interface

- 📱 Multi-Platform Support
  - Web interface
  - WhatsApp integration
  - Responsive design

## Tech Stack

### Frontend
- React 18 with TypeScript
- Material-UI (MUI)
- React Router v6
- Axios for API communication

### Backend
- Flask 2.3.3
- Python 3.8+
- OpenAI API integration
- MongoDB database
- WhatsApp Business API

## Getting Started

### Prerequisites
- Node.js 16+
- Python 3.8+
- MongoDB
- OpenAI API key
- WhatsApp Business API credentials

### Installation

1. Clone the repository:
```bash
git clone https://github.com/vaishnavipattapu/GDC.git
cd GDC
```

2. Install backend dependencies:
```bash
cd GDC
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

### Running the Application

1. Start the backend server:
```bash
cd GDC
python app.py
```

2. Start the frontend development server:
```bash
cd frontend
npm start
```

3. Access the application:
- Web interface: http://localhost:3000
- Backend API: http://localhost:5000

## System Architecture

For detailed system architecture and workflow information, please refer to the [design documentation](docs/design.md).

## API Documentation

### Content Generation
- Endpoint: `POST /api/generate-content`
- Request: `{ subject: string, topic: string, difficulty: string }`
- Response: `{ success: boolean, content: string, content_id: string }`

### Content Retrieval
- Endpoint: `GET /api/content/<content_id>`
- Response: `{ success: boolean, content: object }`

### WhatsApp Webhook
- Endpoint: `POST /api/whatsapp/webhook`
- Request: WhatsApp message payload
- Response: Processed message response

## Security Features

- JWT-based authentication
- Role-based access control
- API key management
- Input sanitization
- CORS configuration
- Rate limiting

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

### Contributors
- [switch41](https://github.com/switch41) - Main contributor and developer

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the AI capabilities
- Meta for WhatsApp Business API
- MongoDB for database support
- The open-source community for various libraries and tools

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Roadmap

- [ ] User authentication system
- [ ] Progress tracking
- [ ] Content recommendations
- [ ] Multi-language support
- [ ] WebSocket for real-time updates
- [ ] GraphQL API
- [ ] Microservices architecture
- [ ] Containerization with Docker
