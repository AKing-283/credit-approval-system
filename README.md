# Credit Approval System

A modern Django-based credit approval system that helps financial institutions evaluate loan applications efficiently.

## 🚀 Features

- Customer registration and management
- Automated loan eligibility checking
- Credit score calculation
- Loan application processing
- Real-time loan status tracking
- RESTful API architecture

## 🛠️ Tech Stack

- Python 3.11+
- Django 5.0
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Celery for async tasks
- Redis for caching

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.11 or higher
- PostgreSQL 15+

## 🚀 Setup and Installation

### Option 1: Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/your-username/credit-approval-system.git
cd credit-approval-system
```

2. Set up environment variables:
```bash
cp .env.example .env
```
Edit the `.env` file with your configuration:
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=credit_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=db
DB_PORT=5432
```

3. Start the services:
```bash
docker-compose up -d
```

4. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

5. Load initial data:
```bash
docker-compose exec web python manage.py loaddata initial_data.json
```

### Option 2: Local Development Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (same as Docker setup)

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Start Celery worker (in a new terminal):
```bash
celery -A credit_approval_system worker -l info
```

## 🏃‍♂️ Running the Application

### API Endpoints

1. **Customer Registration**
```bash
POST /api/customers/register/
```

2. **Check Loan Eligibility**
```bash
POST /api/loans/check-eligibility/
```

3. **Create Loan Application**
```bash
POST /api/loans/create/
```

4. **View Loans**
```bash
GET /api/loans/
```

### Testing the API

1. Start the application (using either Docker or local setup)
2. Use the provided test scripts in `scripts/` directory:
   - `1_fill_data.txt`: Instructions for loading initial data
   - `2_register.txt`: Customer registration steps
   - `3_check_eligibility.txt`: Loan eligibility checking
   - `4_create_loan.txt`: Creating a loan application
   - `5_view_loan.txt`: Viewing loan details

## 📚 API Documentation

Detailed API documentation is available in the `README_API_TESTING.txt` file.

## 🧪 Testing

Run the test suite:
```bash
# Using Docker
docker-compose exec web python manage.py test

# Local setup
python manage.py test
```

## 🔧 Troubleshooting

1. **Database Connection Issues**
   - Check if PostgreSQL is running
   - Verify database credentials in `.env`
   - Ensure database exists

2. **Celery Worker Issues**
   - Check Redis connection
   - Verify Celery configuration in `settings.py`
   - Check worker logs

3. **Docker Issues**
   - Ensure Docker daemon is running
   - Check container logs: `docker-compose logs`
   - Rebuild containers if needed: `docker-compose up -d --build`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, please open an issue in the GitHub repository.

---
*Last updated: March 2024*
