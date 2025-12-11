# Developer Guide

## Codebase Standards
- **Framework**: Django 4.x
- **Style Guide**: PEP 8 (Python), Standard JS (JavaScript).
- **Templating**: Django Template Language (DTL). Use `{% block %}` for inheritance.

## Key Subsystems

### 1. Analytics Engine (`views.analytics_view`)
Analytics are calculated on-the-fly or cached (future optimization).
- **Data aggregation**: Uses Django ORM aggregation (`Count`, `Sum`).
- **Serialization**: Data is serialized to JSON for Chart.js in `views.py`.
- **Visualization**: `analytics_view.html` renders charts.

### 2. Blockchain Implementation (`models.py`)
- **Genesis Block**: Created automatically if the chain is empty (`utils.initialize_chain`).
- **Hashing**: standard SHA-256 via `hashlib`.
- **Proof of Work**: Simple generic algorthim in `Blockchain.proof_of_work`.
- **Verification**: `is_chain_valid()` traverses the linked list of blocks to verify hashes.

### 3. Design System Implementation
- **Base Template**: `dashboard_base.html` defines the layout (sidebar, header, content area).
- **CSS Variables**: Defined in `design-system.css`. DO NOT hardcode colors. usage: `var(--primary-600)`.

### 4. URL Structure (`urls.py`)
- `/dashboard/`: Redirects based on user role.
- `/api/`: JSON endpoints for AJAX calls.
- `/blockchain/`: Ledger access points.

### 5. Custom Template Tags
- `{% load static %}`: For accessing assets.
- `csrf_token`: Mandatory for all forms.

## Adding New Features
1. **Model**: Define schema in `capstone_project/models.py`.
2. **View**: Create logic in `capstone_project/views.py`.
3. **Template**: Create HTML in `templates/` extending `dashboard_base.html`.
4. **URL**: Register path in `capstone_project/urls.py`.
5. **Migration**: Run `makemigrations` and `migrate`.
