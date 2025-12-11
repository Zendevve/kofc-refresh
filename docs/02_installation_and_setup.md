# Installation and Setup Guide

This guide details how to set up the KofC Project locally for development.

## Prerequisites
- **Python 3.8+**
- **Git**
- **Virtual Environment** (recommended)

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Zendevve/kofc-refresh.git
cd kofc-refresh/base
```

### 2. Create and Activate Virtual Environment
It's best practice to run Django projects in an isolated environment.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the `base/` directory (where `manage.py` is).
Add the following configuration:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### 5. Database Setup
Initialize the SQLite database and run migrations.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)
To access the Django admin panel and the main dashboard as an Admin:
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username (e.g., `Mr_Admin`), email, and password.

### 7. Run the Development Server
```bash
python manage.py runserver
```
Access the application at: `http://127.0.0.1:8000/`

## Troubleshooting

### `TemplateDoesNotExist`
Ensure you are running the command from the directory containing `manage.py`.

### Blockchain Initialization Error
If the blockchain fails to load, ensure the database migrations are fully applied. The system automatically initializes a genesis block on the first run.
