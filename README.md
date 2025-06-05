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

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/AKing-283/credit-approval-system.git
cd credit-approval-system
```

2. Set up environment variables:
```bash
cp .env.example .env
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

## 📚 API Documentation

Detailed API documentation is available in the `README_API_TESTING.txt` file.

## 🧪 Testing

Run the test suite:
```bash
docker-compose exec web python manage.py test
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, please open an issue in the GitHub repository.

---
*Last updated: March 2024*
