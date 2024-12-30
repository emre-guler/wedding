# Wedding Memory Collection App

> **Note**: This project was generated with the assistance of AI (Claude 3.5 Sonnet) to create a wedding memory collection application.

A web application for collecting and sharing wedding memories, including photos, videos, and notes from guests.

## Features

- Photo and video upload functionality
- Guest note submission with video messages
- Memory gallery viewing
- Simple and elegant user interface
- Responsive design for all devices

## Technology Stack

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- File Storage: Local storage with JSON for data persistence
- CORS enabled for cross-origin requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/emre-guler/wedding.git
cd wedding-memory-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The server will start at `http://localhost:3000`

## Project Structure

```
wedding-memory-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── uploads/           # Directory for uploaded files
├── index.html         # Main page
├── memories.html      # Memories gallery page
└── notes.html         # Guest notes page
```

## API Endpoints

- `POST /upload` - Upload photos and videos
- `POST /submit_note` - Submit guest notes with video
- `POST /submit_wish` - Submit wishes
- `GET /get_wishes` - Retrieve all wishes
- `GET /uploads/<filename>` - Serve uploaded files

## AI Generation Notice

This project was generated with the assistance of Claude 3.5 Sonnet, an AI language model. The AI helped with:

- Creating the Flask backend structure
- Implementing file upload functionality
- Designing the frontend interface
- Writing API endpoints
- Generating documentation

While the code is functional, it's recommended to review and test thoroughly before deployment in a production environment.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
