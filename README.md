# Knights of Columbus (KofC) Management System

![KofC Logo](base/static/images/kofc_logo.png)

## 📌 Overview
The **KofC Management System** is a robust, full-stack web application designed to modernize the operations of Knights of Columbus councils. It digitizes member management, event planning, attendance tracking, and donation transparently using a built-in blockchain ledger.

> **Project Status**: Active Development 🚀
> **Documentation**: [Full Docs Here](docs/01_introduction.md)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 4.0+

### Installation
1.  **Clone the repo**
    ```bash
    git clone <repository_url>
    cd kofc
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

4.  **Start Server**
    ```bash
    python manage.py runserver
    ```
    Access the dashboard at `http://127.0.0.1:8000/`.

---

## 📚 Documentation
We have meticulous documentation available in the `docs/` directory:

| Document | Description |
|----------|-------------|
| [**Introduction**](docs/01_introduction.md) | High-level overview of features and goals. |
| [**Setup Guide**](docs/02_installation_and_setup.md) | Detailed installation instructions. |
| [**Architecture**](docs/03_system_architecture.md) | System diagrams and project structure. |
| [**Database Schema**](docs/04_database_schema.md) | ER Diagrams and Data Models. |
| [**User Guides**](docs/05_user_guides/) | Manuals for Admins, Officers, and Members. |
| [**Developer Guide**](docs/06_developer_guide.md) | Code standards and adding new features. |
| [**Design System**](docs/07_design_system.md) | CSS variables and UI components. |

---

## ✨ Key Features

### 🛡️ For Administrators
- **Global Dashboard**: View analytics across all councils.
- **Council Management**: Create, edit, and monitor councils.
- **Event Approval**: Review and approve/reject event proposals.
- **Blockchain Ledger**: Audit all donations via an immutable ledger.

### ⚔️ For Officers
- **QR Attendance**: Scan member QR codes at events for instant attendance logging.
- **Recruitment Tracking**: Manage recruits and view lineage trees.
- **Event Proposals**: Submit events for admin approval.

### 🤝 For Members
- **Digital ID**: Unique QR code for identification.
- **Profile Management**: Update personal details and view degree status.
- **Donation History**: Track personal contributions and download receipts.
- **Forums**: Participate in council discussions.

---

## 🛠️ Technology Stack
- **Backend**: Django (Python)
- **Database**: SQLite (Default), scalable to PostgreSQL.
- **Frontend**: HTML5, Vanilla CSS (Custom Design System), JavaScript.
- **Blockchain**: Custom Python implementation (SHA-256 Proof of Work).
- **Visualization**: Chart.js.

---

## 📂 Project Structure
```
kofc/
├── base/                 # Project Configuration (Settings, URLs)
├── capstone_project/     # Main Application Logic
│   ├── models.py         # Database & Blockchain Models
│   ├── views.py          # Request Handlers
│   ├── urls.py           # App Routing
│   ├── templates/        # HTML Templates
│   └── static/           # CSS, JS, Images
├── docs/                 # Documentation
├── media/                # User Uploads
├── manage.py             # Django CLI
└── requirements.txt      # Dependencies
```

---

## 📄 License
This project is proprietary software for the Knights of Columbus.
