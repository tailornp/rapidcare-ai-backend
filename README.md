# RapidCare AI

## Introduction

RapidCare AI is an intelligent triage management system designed to streamline outpatient care in clinics and hospitals. The platform leverages artificial intelligence to help healthcare staff efficiently assess, prioritize, and manage patient cases based on symptom severity and urgency.

## What It Does

- **Automated Patient Triage**: Quickly evaluates patient symptoms and assigns appropriate priority levels
- **Staff Efficiency**: Reduces administrative burden on clinical staff by automating initial patient assessments
- **Smart Prioritization**: Ensures critical cases receive immediate attention while optimizing overall patient flow

RapidCare AI empowers healthcare facilities to deliver faster, more organized care while improving patient outcomes and operational efficiency.

## Tech Stack

### Backend
- **Python** - Runtime environment
- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM for database management
- **PostgreSQL** - Primary database

### AI/ML
- **Ollama** - Local LLM inference

### Development Tools
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Pylint** - Code linting

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- PostgreSQL installed and running
- Ollama installed locally

### Installation Steps

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd rapidcare-ai-backend
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables**
    - Copy `.env.example` to `.env`
    - Update database credentials and other configuration settings

5. **Set up the database**
    ```bash
    # Create database
    createdb rapidcare_db
    
    # Run migrations
    alembic upgrade head
    ```

6. **Start Ollama**
    ```bash
    ollama serve
    ```

7. **Run the application**
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at `http://localhost:8000`