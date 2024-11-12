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
   ```
3. Activate the virtual environment:
   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file for environment variables, including email settings. The `.env` file should include configurations such as:
   ```plaintext
   MAIL_SERVER=smtp.example.com
   MAIL_PORT=587
   MAIL_USE_TLS=true
   MAIL_USERNAME=your-email@example.com
   MAIL_PASSWORD=your-email-password
   ```
6. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. The frontend will run by default on `http://localhost:3000` and should be configured to communicate with the Flask backend on `http://localhost:5000`.

### Running Tests
To run the unit tests for the backend, execute the following command in the `backend` directory:
```bash
python test_app.py
```

## Contact
For questions, reach out at [your-email@example.com].

