# Damercurian Website

This repository contains the backend and frontend code for the Damercurian website, a personal or consulting portfolio platform built using Flask for the backend and React for the frontend.

## Features
- Contact form that sends messages via email.
- Flask backend for server-side logic.
- React frontend for an interactive user experience.
- Unit tests for validating core functionality.

## Technologies Used
- **Backend**: Flask, Flask-Mail, Flask-CORS
- **Frontend**: React
- **Testing**: Unittest and Mocking

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js and npm
- Git

### Backend Setup
1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```bash
   python -m venv venv
3. Activate the virtual environment:
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Create a ```.env file for environment variables, including email settings.

6. Run the Flask server:
python app.py

### Frontend Setup

1. 