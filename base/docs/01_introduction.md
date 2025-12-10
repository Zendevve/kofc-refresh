# Introduction to KofC Project

## Overview
The **Knights of Columbus (KofC) Management System** is a comprehensive web application designed to digitize and streamline the operations of the Knights of Columbus districts and councils. It serves as a centralized platform for managing members, events, donations, and administrative tasks, fostering better communication and transparency within the organization.

## Key Features

### 1. Membership Management
- **Role-based Access**: Custom dashboards for Admins, Officers, and Members.
- **Recruitment Tracking**: Track recruitment history and lineage (who recruited whom).
- **Digital Profiles**: Manage member details including degree, council affiliation, and contact info.
- **Attendance Tracking**: QR-code based attendance system for events.

### 2. Event Management
- **Event Creation & Approval**: Officers can propose events; Admins approve them.
- **Calendar View**: Comprehensive list of upcoming and past events.
- **Participation Analytics**: Track member engagement and event success.

### 3. Donation System & Blockchain Transparency
- **Transparent Ledger**: All donations are recorded on a custom **Blockchain Ledger** to ensure immutability and trust.
- **Payment Integration**: Support for GCash and manual donation entry.
- **Receipts**: Auto-generated digital receipts for donors.
- **Analytics**: Visualization of donation trends, sources, and fund forecasting.

### 4. Communication & Engagement
- **Forums**: Role-specific discussion boards (General, Announcements, Urgent).
- **Notifications**: Real-time alerts for approvals, messages, and events.
- **Gamification**: Activity rankings and leaderboards to encourage participation.

## Technology Stack
- **Backend**: Django (Python)
- **Database**: SQLite (Development), PostgreSQL (Production ready)
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), JavaScript
- **Visualization**: Chart.js for analytics
- **Cryptography**: Python `cryptography` library for blockchain signing and verification.

## Target Audience
- **District Directors (Admins)**: Oversee multiple councils, approve events, view global analytics.
- **Grand Knights (Officers)**: Manage council events, take attendance, recruit members.
- **Knights (Members)**: View events, donate, track own activities.
