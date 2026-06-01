# Secure Authentication System

## Project Overview

Secure Authentication System is a full-stack authentication platform built using Flask, PostgreSQL, JWT, Bcrypt, and Resend API. The system provides secure user registration, login, email verification, password reset, and protected API access using industry-standard security practices.

The application demonstrates modern authentication workflows commonly used in real-world web applications and enterprise systems.

---

# Application Screenshots

## Home Page

![Home Page](Screenshot/HOMEPAGE.png)

---

## Login Page

![Login Page](Screenshot/LOGINPAGE.png)

---

## Email Verification Email

![Email Verification](Screenshot/EMAILVERIFICATION.png)

---

## Email Verification Success

![Email Verification Success](Screenshot/EMAILVERIFICATIONSUCCESS.png)

---

## Forgot Password

![Forgot Password](Screenshot/forgot.png)

---

## Password Reset

![Password Reset](Screenshot/newpass.png)

---

## Successful Login Dashboard

![Dashboard](Screenshot/successlogin.png)

---

# Features

## Authentication Features

* User Registration
* User Login Authentication
* User Logout
* JWT Access Token Generation
* JWT Refresh Token Generation
* JWT Token Validation
* Protected Routes
* Session Management

---

## Security Features

* Password Hashing using Bcrypt
* JWT-Based Authentication
* Secure Password Storage
* Input Validation
* Error Handling
* SQL Injection Prevention using SQLAlchemy ORM
* Environment Variable Configuration
* Token-Based Access Control

---

## Email Features

* Email Verification
* Verification Token Generation
* Resend Email Integration
* Forgot Password Functionality
* Password Reset Email
* Secure Password Reset Links

---

## Database Features

* PostgreSQL Integration
* User Account Storage
* Verification Token Storage
* Authentication Data Management
* Database Migrations using Flask-Migrate

---

## Deployment Features

* Backend Deployment using Render
* Frontend Deployment using Netlify
* CORS Configuration
* Production Environment Variable Management

---

# Technologies Used

## Backend

* Python
* Flask
* Flask-JWT-Extended
* Flask-Bcrypt
* Flask-Migrate
* Flask-CORS
* SQLAlchemy
* Python-Dotenv

---

## Database

* PostgreSQL

---

## Authentication

* JWT (JSON Web Tokens)
* Bcrypt Password Encryption

---

## Email Service

* Resend API

---

## Deployment

* Render
* Netlify

---

# System Architecture

```text
Frontend (Netlify)

        │

        ▼

Flask Backend API

        │

        ▼

JWT Authentication Layer

        │

        ▼

PostgreSQL Database

        │

        ▼

Email Verification &
Password Reset Services
```

---

# Authentication Workflow

## User Registration

1. User enters username, email, and password.
2. Input validation is performed.
3. Password is hashed using Bcrypt.
4. User account is stored in PostgreSQL.
5. Verification token is generated.
6. Verification email is sent.
7. User verifies the account using the verification link.

---

## User Login

1. User enters email and password.
2. Password hash is verified.
3. Account verification status is checked.
4. JWT Access Token is generated.
5. JWT Refresh Token is generated.
6. User receives authentication tokens.

---

## Email Verification Workflow

1. User registers an account.
2. Verification token is generated.
3. Verification email is sent.
4. User clicks the verification link.
5. Account is marked as verified.
6. User can successfully log in.

---

## Password Reset Workflow

1. User requests a password reset.
2. Reset token is generated.
3. Password reset email is sent.
4. User opens the reset link.
5. User enters a new password.
6. Password is securely updated.

---

# Database Schema

## Users Table

| Field              | Type      |
| ------------------ | --------- |
| id                 | Integer   |
| username           | String    |
| email              | String    |
| password           | String    |
| role               | String    |
| is_verified        | Boolean   |
| verification_token | String    |
| created_at         | Timestamp |

---

## Password Reset Table

| Field       | Type      |
| ----------- | --------- |
| id          | Integer   |
| user_id     | Integer   |
| reset_token | String    |
| expires_at  | Timestamp |
| is_used     | Boolean   |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/secure-auth-system.git
```

## Navigate to Project Directory

```bash
cd secure-auth-system
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret_key

DATABASE_URL=postgresql://username:password@localhost/database_name

RESEND_API_KEY=your_resend_api_key
```

---

# Running the Application

```bash
python run.py
```

Application runs at:

```text
http://localhost:5000
```

---

# API Endpoints

## Authentication

### Register User

```http
POST /api/auth/register
```

### Login User

```http
POST /api/auth/login
```

### Logout User

```http
POST /api/auth/logout
```

### Refresh Token

```http
POST /api/auth/refresh
```

---

## Email Verification

### Verify Email

```http
GET /api/auth/verify-email/<token>
```

### Resend Verification Email

```http
POST /api/auth/resend-verification
```

---

## Password Reset

### Forgot Password

```http
POST /api/auth/forgot-password
```

### Reset Password

```http
POST /api/auth/reset-password/<token>
```

---

# Security Features

* Password Hashing using Bcrypt
* JWT Authentication
* Access Token Management
* Refresh Token Management
* Protected API Routes
* Email Verification
* Password Reset Tokens
* SQLAlchemy ORM Protection
* Environment Variable Security
* Secure Authentication Workflow

---

# Project Outcome

Successfully developed a secure authentication system using Flask, JWT, Bcrypt, PostgreSQL, and Resend API.

The application provides:

* Secure User Registration
* Secure User Login
* JWT-Based Authentication
* Access and Refresh Token Management
* Email Verification
* Password Reset Functionality
* Protected Resource Access
* PostgreSQL Database Integration
* Secure Session Management

The project demonstrates industry-standard authentication and authorization practices used in modern web applications.

---

# Future Enhancements

* Two-Factor Authentication (2FA)
* Google OAuth Login
* GitHub OAuth Login
* Account Lockout Protection
* Login Activity Tracking
* Multi-Device Session Management
* Rate Limiting
* Admin Dashboard
* Audit Logging

---

# Author

**Nandini**
