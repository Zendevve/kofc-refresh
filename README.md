<div align="center">

# ⛪ Knights of Columbus Management System

### A Modern Full-Stack Web Platform for Catholic Fraternal Organizations

[![Django](https://img.shields.io/badge/Django-5.2.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Blockchain](https://img.shields.io/badge/Blockchain-SHA--256%20PoW-6D28D9?style=for-the-badge&logo=ethereum&logoColor=white)](#-blockchain-powered-donations)
[![License](https://img.shields.io/badge/License-Proprietary-DC2626?style=for-the-badge)](#-license)

*Digitizing faith-based organization management with transparent donation tracking, intelligent analytics, and seamless member engagement.*

<img src="capstone_project/static/images/main-logo.png" alt="KofC Logo" width="180"/>

[Features](#-key-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [Documentation](#-documentation) • [Screenshots](#-screenshots)

</div>

---

## 🌟 What is This?

The **Knights of Columbus Management System** is a comprehensive web application that transforms how Catholic councils operate. It replaces scattered spreadsheets and paper trails with a unified digital platform—complete with a **blockchain-backed donation ledger** for unparalleled financial transparency.

> **Who is this for?**
> • **Council Administrators**: Oversee multiple councils from a single dashboard
> • **Officers (Grand Knights)**: Manage events, track attendance, recruit members
> • **Members (Knights)**: Stay engaged, donate, and track their journey

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔐 Role-Based Access Control
- **Admin Dashboard**: Global analytics, council oversight, event approvals
- **Officer Portal**: Event management, QR attendance, recruitment tools
- **Member Hub**: Personal profile, donation history, activity tracking

### 📊 Intelligent Analytics
- **Predictive Forecasting**: 6-month donation and recruitment projections
- **Engagement Metrics**: Activity rankings, participation heatmaps
- **Source Analysis**: Donation distribution by member type

</td>
<td width="50%">

### ⛓️ Blockchain-Powered Donations
- **Immutable Ledger**: SHA-256 Proof-of-Work chain
- **Cryptographic Signatures**: RSA-signed transactions
- **Full Transparency**: Public audit trail for all contributions

### 📱 Modern Member Experience
- **QR-Code Attendance**: Instant event check-in via camera scan
- **Digital ID Cards**: Unique QR codes for each member
- **Real-Time Notifications**: Event reminders, approvals, forum alerts

</td>
</tr>
</table>

### Additional Highlights
- 📅 **Event Lifecycle Management**: Proposal → Approval → Attendance → Analytics
- 👥 **Recruitment Lineage Trees**: Visualize who recruited whom
- 💬 **Council Forums**: Category-based discussions with pinned announcements
- 🏆 **Gamified Leaderboards**: Rank members by engagement and contributions
- 📜 **Auto-Generated Receipts**: Professional donation receipts with e-signatures

### 🆕 Recent Updates (December 2025)
- **Improved Donation Review UI**: Styled rejection modal with categorized reasons dropdown matching event rejection workflow
- **Self-Review Prevention**: Users can now see their own pending donations but cannot approve/reject them (segregation of duties)
- **UI Fixes**: Fixed button hover states for Update Event and Logout buttons

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/kofc.git
cd kofc

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate cryptographic keys (for blockchain signing)
python generate_keys.py

# 5. Apply database migrations
python manage.py migrate

# 6. Create a superuser (optional)
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

🎉 **That's it!** Access the app at `http://127.0.0.1:8000/`

### Demo Accounts
| Role | Username | Password |
|------|----------|----------|
| Admin | `Mr_Admin` | *Set during setup* |

---

## 🏗️ Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Browser                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   HTML5     │  │   CSS3      │  │   JavaScript + Chart.js │ │
│  │  Templates  │  │  Design     │  │   (Analytics, QR Scan)  │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/HTTPS
┌────────────────────────────┴────────────────────────────────────┐
│                    Django Application (v5.2.1)                  │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────────────────┐  │
│  │   Views     │  │   Models    │  │   Blockchain Engine    │  │
│  │  (Request   │  │  (ORM for   │  │  (SHA-256 PoW Mining,  │  │
│  │  Handlers)  │  │  SQLite/PG) │  │   RSA Signatures)      │  │
│  └─────────────┘  └─────────────┘  └────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
         ┌───────────────────┴───────────────────┐
         ▼                                       ▼
┌─────────────────────┐               ┌─────────────────────┐
│     SQLite/PostgreSQL│              │  Blockchain Ledger  │
│  (Members, Events,  │               │  (Donation Blocks,  │
│   Councils, etc.)   │               │   Transaction Hashes│
└─────────────────────┘               └─────────────────────┘
```

### Project Structure

```
kofc/
├── capstone_project/        # Main application
│   ├── models.py            # User, Council, Event, Donation, Block, Blockchain
│   ├── views.py             # Primary request handlers
│   ├── more_views/          # Modular view extensions
│   │   ├── attendance.py    # QR attendance logic
│   │   ├── council.py       # Council CRUD operations
│   │   └── api_endpoints.py # AJAX/JSON endpoints
│   ├── templates/           # 57+ HTML templates
│   ├── static/              # CSS, JS, images
│   └── templatetags/        # Custom Django filters
├── docs/                    # Comprehensive documentation
├── media/                   # User uploads (receipts, profiles)
├── manage.py                # Django CLI
├── requirements.txt         # Python dependencies
├── private_key.pem          # RSA private key (blockchain signing)
└── public_key.pem           # RSA public key (signature verification)
```

### Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django 5.2.1, Python 3.8+ |
| **Database** | SQLite (dev), PostgreSQL (production-ready) |
| **Frontend** | HTML5, Vanilla CSS3, JavaScript ES6+ |
| **Blockchain** | Custom Python implementation (SHA-256 PoW) |
| **Cryptography** | RSA (4096-bit) via `cryptography` library |
| **Visualization** | Chart.js for analytics dashboards |
| **Data Processing** | pandas for trend analysis and forecasting |
| **Image Processing** | Pillow for profile/receipt handling |

---

## 📚 Documentation

Complete technical documentation is available in the `docs/` directory:

| Document | Description |
|----------|-------------|
| [📖 Introduction](docs/01_introduction.md) | Feature overview and target audience |
| [🔧 Installation Guide](docs/02_installation_and_setup.md) | Detailed setup instructions |
| [🏛️ System Architecture](docs/03_system_architecture.md) | Component diagrams and data flow |
| [🗃️ Database Schema](docs/04_database_schema.md) | ER diagrams and model relationships |
| [📘 Admin Guide](docs/05_user_guides/) | Role-specific user manuals |
| [💻 Developer Guide](docs/06_developer_guide.md) | Code standards and contribution guidelines |
| [🎨 Design System](docs/07_design_system.md) | CSS variables, components, and styling |

---

## 🖼️ Screenshots

> *Screenshots coming soon — the application features a modern, responsive design with dark/light mode support.*

<details>
<summary>📊 Admin Analytics Dashboard</summary>

- Donation trend charts with 6-month forecasting
- Member engagement heatmaps
- Event participation metrics
- Blockchain health status

</details>

<details>
<summary>📱 QR Attendance System</summary>

- Officer scans member QR codes via camera
- Real-time attendance logging
- Digital member ID card with unique QR

</details>

<details>
<summary>⛓️ Blockchain Donation Ledger</summary>

- Immutable transaction history
- Block explorer with hash verification
- Proof-of-Work validation status

</details>

---

## 🔐 Security Features

- **RSA-4096 Digital Signatures**: All donations cryptographically signed
- **Immutable Blockchain Ledger**: Tamper-proof transaction history
- **Role-Based Permissions**: Granular access control per user type
- **Secure File Uploads**: Validated image uploads for profiles/receipts
- **CSRF Protection**: Django's built-in cross-site request forgery prevention

---

## 🛠️ For Developers

### Running Tests

```bash
python manage.py test capstone_project
```

### Key Models
- **`User`**: Extended Django AbstractUser with roles, councils, degrees
- **`Council`**: District-based organizational units
- **`Event`**: Lifecycle-managed events with approval workflow
- **`Donation`**: RSA-signed contributions with blockchain integration
- **`Block` / `Blockchain`**: Custom PoW blockchain implementation
- **`Recruitment`**: Lineage tracking (recruiter → recruit relationships)

### API Endpoints
The `more_views/api_endpoints.py` module provides JSON endpoints for:
- Member search and filtering
- Donation analytics aggregation
- Attendance status checks
- Notification counts

---

## 🤝 Contributing

This is a proprietary project for the Knights of Columbus organization. For authorized contributors:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is **proprietary software** developed for the Knights of Columbus.
All rights reserved.

---

<div align="center">

### Built with ❤️ for Faith-Based Organizations

*"In service to One. In service to all."*

**Questions?** Contact the development team.

</div>
